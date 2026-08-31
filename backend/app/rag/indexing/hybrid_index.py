import math
from typing import List, Dict, Any


class HybridSearchIndex:
    """
    Simulates combined dense vector embedding retrieval + sparse BM25 keyword search
    using Reciprocal Rank Fusion (RRF).
    """
    def __init__(self):
        self.documents: List[Dict[str, Any]] = []

    def add_chunks(self, chunks: List[Dict[str, Any]]) -> None:
        self.documents.extend(chunks)

    def search_hybrid(self, query: str, top_k: int = 5, rrf_k: int = 60) -> List[Dict[str, Any]]:
        query_words = set(query.lower().split())
        scored_docs = []

        for doc in self.documents:
            content_lower = doc.get("content", "").lower()
            # Simple keyword score
            bm25_score = sum(1.0 for w in query_words if w in content_lower)
            # Simulated dense vector similarity score
            dense_score = len(set(query_words) & set(content_lower.split())) / (len(query_words) or 1)
            # RRF combined score
            rrf_score = (1.0 / (rrf_k + (1.0 / (bm25_score + 0.01)))) + (1.0 / (rrf_k + (1.0 / (dense_score + 0.01))))
            
            scored_docs.append({
                **doc,
                "score": round(rrf_score, 4),
                "bm25_score": bm25_score,
                "dense_score": round(dense_score, 4)
            })

        scored_docs.sort(key=lambda x: x["score"], reverse=True)
        return scored_docs[:top_k]


hybrid_search = HybridSearchIndex()
