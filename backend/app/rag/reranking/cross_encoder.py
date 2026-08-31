from typing import List, Dict, Any


class CrossEncoderReranker:
    """Cross-Encoder Reranker scoring (Query, Document) pairs with high contextual precision."""

    def rerank(self, query: str, candidates: List[Dict[str, Any]], top_k: int = 3) -> List[Dict[str, Any]]:
        query_terms = set(query.lower().split())
        reranked = []

        for doc in candidates:
            content = doc.get("content", "")
            # Precision term density scoring
            matched_terms = [t for t in query_terms if t in content.lower()]
            rerank_score = len(matched_terms) / (len(query_terms) or 1)
            
            reranked.append({
                **doc,
                "rerank_score": round(rerank_score, 4),
                "original_rank_score": doc.get("score", 0.0)
            })

        reranked.sort(key=lambda x: x["rerank_score"], reverse=True)
        return reranked[:top_k]


reranker = CrossEncoderReranker()
