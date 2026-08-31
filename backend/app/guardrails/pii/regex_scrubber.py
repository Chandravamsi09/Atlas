import re
from typing import Tuple, Dict


class PIIScrubber:
    """High-accuracy PII detector and anonymizer for SSNs, Emails, Phones, and API Keys."""

    # Execute SSN and Credit Cards before Phone to avoid partial overlaps
    PATTERNS = [
        ("SSN", r"\b\d{3}-\d{2}-\d{4}\b"),
        ("CREDIT_CARD", r"\b(?:\d{4}[-\s]?){3}\d{4}\b"),
        ("EMAIL", r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
        ("API_KEY", r"\b(sk-[a-zA-Z0-9]{20,48}|atl_live_[a-zA-Z0-9_-]{20,60})\b"),
        ("PHONE", r"\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"),
    ]

    def sanitize(self, text: str) -> Tuple[str, Dict[str, int]]:
        counts: Dict[str, int] = {}
        sanitized = text

        for pii_type, pattern in self.PATTERNS:
            matches = re.findall(pattern, sanitized, re.IGNORECASE)
            if matches:
                counts[pii_type] = len(matches)
                sanitized = re.sub(pattern, f"<REDACTED_{pii_type}>", sanitized, flags=re.IGNORECASE)

        return sanitized, counts


pii_scrubber = PIIScrubber()
