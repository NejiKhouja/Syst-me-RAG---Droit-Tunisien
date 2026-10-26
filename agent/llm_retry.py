import re
import time

MAX_RETRIES = 3       # retries after the first attempt, on rate limits (429) only
MAX_WAIT_S = 120      # a longer wait (e.g. the daily token limit) fails at once instead of blocking


class LLMRateLimitError(RuntimeError):
    pass


def _is_rate_limit(e: Exception) -> bool:
    msg = str(e).lower()
    return "429" in msg or "rate limit" in msg or "rate_limit" in msg or e.__class__.__name__ == "RateLimitError"


def _stated_wait(msg: str) -> float | None:
    """Groq says e.g. 'Please try again in 3m50.25s' or '850ms'."""
    m = re.search(r"try again in\s+(?:(\d+)h)?\s*(?:(\d+)m(?!s))?\s*(?:([\d.]+)s)?\s*(?:([\d.]+)ms)?", msg)
    if not m or not any(m.groups()):
        return None
    h, mi, s, ms = (float(x) if x else 0.0 for x in m.groups())
    return h * 3600 + mi * 60 + s + ms / 1000


def invoke_with_retry(runnable, messages, what: str, sleep=time.sleep):
    """runnable.invoke(messages), retrying up to MAX_RETRIES times on 429 with backoff.
    Other errors propagate unchanged. After the retries, raise LLMRateLimitError with a clear message."""
    for attempt in range(MAX_RETRIES + 1):
        try:
            return runnable.invoke(messages)
        except Exception as e:
            if not _is_rate_limit(e):
                raise
            wait = _stated_wait(str(e))
            wait = (wait + 1) if wait is not None else 5 * 2 ** attempt     # 5, 10, 20 s when Groq gives no hint
            if attempt == MAX_RETRIES or wait > MAX_WAIT_S:
                raise LLMRateLimitError(
                    f"{what}: Groq rate limit (429) after {attempt} retr{'y' if attempt == 1 else 'ies'}: {str(e)[:200]}\n"
                    f"Re-run the same command, completed items are cached.") from e
            sleep(wait)
