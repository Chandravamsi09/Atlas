from typing import List, Dict, Any


class DocumentLoader:
    """Parser and text extractor for Markdown, Text, PDF, Code, and HTML documents."""
    
    def load_text(self, text: str, source_title: str) -> Dict[str, Any]:
        return {
            "title": source_title,
            "content": text,
            "char_count": len(text),
            "line_count": len(text.splitlines())
        }


doc_loader = DocumentLoader()
