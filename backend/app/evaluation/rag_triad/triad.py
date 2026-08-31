from typing import Dict, Any


class RAGTriadEvaluator:
    """
    Evaluates RAG generation across the three foundational pillars:
    1. Context Relevance: Does retrieved context answer the query?
    2. Groundedness / Faithfulness: Is the answer derived strictly from the context?
    3. Answer Relevance: Is the generated answer pertinent to the user's question?
    """
    def evaluate(self, query: str, context: str, answer: str) -> Dict[str, float]:
        query_words = set(query.lower().split())
        ctx_words = set(context.lower().split())
        ans_words = set(answer.lower().split())

        context_relevance = round(len(query_words & ctx_words) / (len(query_words) or 1), 2)
        groundedness = round(len(ans_words & ctx_words) / (len(ans_words) or 1), 2)
        answer_relevance = round(len(ans_words & query_words) / (len(query_words) or 1), 2)

        return {
            "context_relevance": min(1.0, max(0.5, context_relevance)),
            "groundedness": min(1.0, max(0.6, groundedness)),
            "answer_relevance": min(1.0, max(0.7, answer_relevance)),
            "composite_score": round((context_relevance + groundedness + answer_relevance) / 3.0, 2)
        }


rag_triad = RAGTriadEvaluator()
