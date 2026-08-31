# Enterprise Hybrid RAG Best Practices

## 1. Hybrid Search Architecture
To achieve state-of-the-art retrieval accuracy:
1. **Dense Vector Search**: Captures high-level semantic intent using pgvector HNSW indexes.
2. **Sparse BM25 Search**: Matches exact keywords, technical identifiers, and part numbers.
3. **Reciprocal Rank Fusion (RRF)**: Merges ranked candidate lists without calibration drift.
4. **Cross-Encoder Reranker**: Performs deep contextual joint scoring on the top-20 candidates.
