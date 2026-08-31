from sqlalchemy import String, Boolean, ForeignKey, JSON, Integer, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.db.base import Base


class GuardrailRule(Base):
    __tablename__ = "guardrail_rules"

    org_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    rule_type: Mapped[str] = mapped_column(String(50), nullable=False) # pii, injection, toxicity, json_schema, regex
    phase: Mapped[str] = mapped_column(String(20), default="input", nullable=False) # input, output
    action: Mapped[str] = mapped_column(String(20), default="block", nullable=False) # block, mask, alert
    config: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    organization = relationship("Organization", back_populates="guardrails")


class GuardrailLog(Base):
    __tablename__ = "guardrail_logs"

    org_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    rule_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    violation_type: Mapped[str] = mapped_column(String(50), nullable=False)
    phase: Mapped[str] = mapped_column(String(20), nullable=False)
    action_taken: Mapped[str] = mapped_column(String(20), nullable=False)
    matched_snippet: Mapped[str] = mapped_column(Text, nullable=True)
    request_id: Mapped[str] = mapped_column(String(64), nullable=True, index=True)
