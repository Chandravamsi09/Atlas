from sqlalchemy import String, Boolean, ForeignKey, JSON, Integer, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.db.base import Base


class TenantQuota(Base):
    __tablename__ = "tenant_quotas"

    org_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), unique=True, nullable=False)
    monthly_budget_usd: Mapped[float] = mapped_column(Float, default=1000.0, nullable=False)
    current_spend_usd: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    monthly_token_limit: Mapped[int] = mapped_column(Integer, default=100_000_000, nullable=False)
    current_token_usage: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    rate_limit_rps: Mapped[int] = mapped_column(Integer, default=100, nullable=False)
    alert_threshold_pct: Mapped[int] = mapped_column(Integer, default=80, nullable=False)
    hard_limit_enabled: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    organization = relationship("Organization", back_populates="quota")
