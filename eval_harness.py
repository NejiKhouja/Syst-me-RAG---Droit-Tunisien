"""Evaluation-side plumbing: reproducible LLM calls and run-health tracking.

The pipeline code is left untouched. During an eval run we swap translate._get_llm
for a wrapper that (a) forces a temperature if asked, (b) caches outputs on disk
keyed by hash(prompt + model + temperature [+ salt when temperature > 0]), and (c) retries with backoff
on Groq errors (rate limits).
"""
import hashlib
import json
import logging
import re
import sys
import time
from pathlib import Path

from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq

from config import GROQ_API_KEY, LLM_MODEL


def _retry_after_seconds(message: str) -> float | None:
    """Parse Groq's 'Please try again in 3m50.25s' / '1h2m3s' / '850ms' hint."""
    m = re.search(r"try again in\s+(?:(\d+)h)?\s*(?:(\d+)m(?!s))?\s*(?:([\d.]+)s)?\s*(?:([\d.]+)ms)?", message)
    if not m or not any(m.groups()):
        return None
    h, mi, sec, ms = (float(x) if x else 0.0 for x in m.groups())
    return h * 3600 + mi * 60 + sec + ms / 1000


class LLMStats:
    def __init__(self) -> None:
        self.calls = 0
        self.cache_hits = 0
        self.temps: set[float] = set()


def install_llm_cache(
    translate_module,
    temperature: float | None,
    cache_path: Path | None,
    salt: str = "",
    max_retries: int = 8,
    max_tokens: int = 2000,
    max_wait_s: float = 4 * 3600,
) -> LLMStats:
    """temperature=None keeps the pipeline's own temperatures (0.0 rewrite, 0.3 sub-queries)."""
    stats = LLMStats()
    cache: dict[str, str] = {}
    if cache_path and cache_path.exists():
        cache = json.loads(cache_path.read_text(encoding="utf-8"))

    def make(requested: float):
        temp = requested if temperature is None else temperature
        # max_tokens only caps the output reserved against Groq's per-minute token budget
        # (the default reservation would let one call starve the next); prompts/model/temperature are unchanged.
        llm = ChatGroq(api_key=GROQ_API_KEY, model_name=LLM_MODEL, temperature=temp, max_tokens=max_tokens)

        def run(prompt_value):
            msgs = prompt_value.to_messages()
            # The salt separates independent samples of NON-deterministic calls only (temperature > 0);
            # temperature-0 outputs are shared across runs.
            key = hashlib.sha256(f"{msgs}|{LLM_MODEL}|{temp}|{salt if temp > 0 else ''}".encode()).hexdigest()
            stats.temps.add(temp)
            if cache_path and key in cache:
                stats.cache_hits += 1
                return cache[key]
            attempts, waited = 0, 0.0
            while True:
                try:
                    stats.calls += 1
                    out = llm.invoke(msgs).content
                    if cache_path:
                        cache[key] = out
                        cache_path.parent.mkdir(parents=True, exist_ok=True)
                        cache_path.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")
                    return out
                except Exception as exc:
                    msg = str(exc)
                    stated = _retry_after_seconds(msg) if "429" in msg else None
                    if stated is not None:
                        # Rate limit (per-minute or daily tokens): wait exactly as long as Groq says, never
                        # give up early and never fall back silently (bounded by max_wait_s per call).
                        wait = stated + 2
                        waited += wait
                        if waited > max_wait_s:
                            raise RuntimeError(f"LLM rate limit did not clear within {max_wait_s}s") from exc
                        kind = "daily" if "(TPD)" in msg else "per-minute/request"
                        print(f"  [rate limit ({kind}); waiting {wait:.0f}s]", file=sys.stderr, flush=True)
                        time.sleep(wait)
                        continue
                    attempts += 1
                    if attempts >= max_retries:
                        raise RuntimeError("LLM call failed after retries") from exc
                    wait = min(60, 2 ** attempts * 2)
                    print(f"  [llm retry {attempts}/{max_retries} in {wait}s: {msg[:80]}]", file=sys.stderr)
                    time.sleep(wait)

        return RunnableLambda(run)

    translate_module._get_llm = lambda temperature=0.0: make(0.0 if temperature == 0.0 else 0.3)
    translate_module._rewrite_cache.clear()
    translate_module._subquery_cache.clear()
    return stats


class DegradationCounter(logging.Handler):
    """Counts the WARNINGs the pipeline emits when a component silently falls back."""

    def __init__(self) -> None:
        super().__init__(level=logging.WARNING)
        self.events: list[str] = []

    def emit(self, record: logging.LogRecord) -> None:
        if record.name in ("translate", "reranker"):
            self.events.append(f"{record.name}: {record.getMessage()[:160]}")

    def attach(self) -> "DegradationCounter":
        for name in ("translate", "reranker"):
            logging.getLogger(name).addHandler(self)
        return self
