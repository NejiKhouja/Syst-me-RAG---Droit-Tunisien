import logging
from langchain_core.documents import Document
from sentence_transformers import CrossEncoder

from config import RERANKER_MODEL, RERANK_TOP_K, RERANK_MAX_LENGTH, RERANK_QUANTIZE, RERANK_BATCH

logger = logging.getLogger(__name__)

_reranker: CrossEncoder | None = None


def get_reranker() -> CrossEncoder:
    global _reranker
    if _reranker is None:
        logger.info("Loading cross-encoder: %s (max_length=%d, int8=%s)",
                    RERANKER_MODEL, RERANK_MAX_LENGTH, RERANK_QUANTIZE)
        model = CrossEncoder(RERANKER_MODEL, max_length=RERANK_MAX_LENGTH)
        if RERANK_QUANTIZE:
            import torch
            torch.quantization.quantize_dynamic(model.model, {torch.nn.Linear}, dtype=torch.qint8, inplace=True)
        _reranker = model
    return _reranker


def rerank(query: str, docs: list[Document], top_k: int = RERANK_TOP_K) -> list[Document]:
    """Order docs by cross-encoder relevance and keep the best top_k.

    Fails loudly: if the model cannot be loaded or scored, the exception propagates. (v1 swallowed errors and
    silently returned the unranked candidates; it also crashed whenever fewer than top_k candidates existed.)
    """
    if not docs:
        return docs
    scores = get_reranker().predict(
        [(query, doc.page_content) for doc in docs], batch_size=RERANK_BATCH, show_progress_bar=False
    )
    ranked = sorted(zip(scores, docs), key=lambda x: x[0], reverse=True)
    logger.debug("Reranked %d -> %d docs | top score=%.3f", len(docs), min(top_k, len(ranked)), ranked[0][0])
    return [doc for _, doc in ranked[:top_k]]
