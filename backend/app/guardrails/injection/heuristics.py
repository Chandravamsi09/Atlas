import re
from typing import Tuple


class PromptInjectionDetector:
    """
    Rule-based and heuristic detector for adversarial prompt injection,
    jailbreak attempts, and system prompt extraction attacks.
    """
    SUSPICIOUS_PATTERNS = [
        r"ignore\s+(all\s+)?(previous|prior)\s+instructions",
        r"disregard\s+(all\s+)?rules",
        r"system\s*prompt\s*(override|extraction)",
        r"(dan\s+mode|unrestricted|god\s+mode)",
        r"reveal\s+(your\s+)?(secret|initial|developer)\s+instructions",
        r"print\s+system\s+prompt",
        r"bypass\s+(all\s+)?(safety|content)\s+filters",
        r"base64\s*decode\s*the\s*following",
    ]

    def check_injection(self, text: str) -> Tuple[bool, str]:
        for pattern in self.SUSPICIOUS_PATTERNS:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return True, f"Detected injection signature: '{match.group(0)}'"
        return False, ""


injection_detector = PromptInjectionDetector()
