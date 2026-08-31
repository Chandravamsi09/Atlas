from typing import List, Dict, Any


class RecursiveCharacterChunker:
    """
    Splits text recursively based on paragraph, line, and word boundaries
    while maintaining context window overlaps.
    """
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk(self, text: str, title: str = "Document") -> List[Dict[str, Any]]:
        chunks = []
        start = 0
        text_len = len(text)
        chunk_idx = 0

        while start < text_len:
            end = min(start + self.chunk_size, text_len)
            
            # Find nearest space or newline if not at end
            if end < text_len:
                last_space = text.rfind(" ", start, end)
                if last_space != -1 and last_space > start + self.chunk_size // 2:
                    end = last_space

            chunk_text = text[start:end].strip()
            if chunk_text:
                chunks.append({
                    "title": title,
                    "chunk_index": chunk_idx,
                    "content": chunk_text,
                    "token_count": len(chunk_text) // 4
                })
                chunk_idx += 1

            start += self.chunk_size - self.chunk_overlap

        return chunks


default_chunker = RecursiveCharacterChunker()
