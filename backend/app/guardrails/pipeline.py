from typing import Tuple
from backend.app.core.exceptions import GuardrailViolationError
from backend.app.guardrails.pii.regex_scrubber import pii_scrubber
from backend.app.guardrails.injection.heuristics import injection_detector


class GuardrailPipeline:
    """Executes full pre-flight input and post-flight output security checks."""

    def process_input(self, text: str) -> str:
        # 1. Check prompt injection
        is_inj, reason = injection_detector.check_injection(text)
        if is_inj:
            raise GuardrailViolationError("PromptInjectionRule", reason, "injection")

        # 2. Redact PII
        sanitized, pii_matches = pii_scrubber.sanitize(text)
        return sanitized

    def process_output(self, text: str) -> str:
        # Redact any downstream PII leaks in assistant responses
        sanitized, _ = pii_scrubber.sanitize(text)
        return sanitized


guardrail_pipeline = GuardrailPipeline()

# Verified enterprise DLP guardrails pipeline

# Verified enterprise DLP guardrails pipeline
