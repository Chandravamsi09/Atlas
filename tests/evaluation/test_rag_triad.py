import pytest
from backend.app.evaluation.rag_triad.triad import rag_triad


def test_rag_triad_evaluation():
    query = "What is the refund policy duration?"
    context = "Our customer refund policy duration is 30 days from purchase date."
    answer = "The refund policy duration is 30 days."

    scores = rag_triad.evaluate(query, context, answer)
    assert scores["context_relevance"] > 0.0
    assert scores["groundedness"] > 0.0
    assert scores["answer_relevance"] > 0.0
    assert scores["composite_score"] > 0.5
