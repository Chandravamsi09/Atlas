# Atlas Safety Guardrails & Security Architecture

## 1. Security Tenets
- **Zero PII Exposure**: Dual-phase regex and NER masking filters sensitive data before provider egress.
- **Adversarial Jailbreak Defense**: Real-time signature detection for prompt injection vectors.
- **Multi-Tenant Isolation**: Row-level tenant context enforcement preventing cross-tenant data leakage.
