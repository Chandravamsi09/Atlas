from sqlalchemy import String, Boolean, ForeignKey, JSON, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column
from backend.app.db.base import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    org_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    actor_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    action: Mapped[str] = mapped_column(String(100), nullable=False) # e.g. "prompt.deploy", "api_key.create"
    resource_type: Mapped[str] = mapped_column(String(50), nullable=False)
    resource_id: Mapped[str] = mapped_column(String(64), nullable=True)
    details: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
    ip_address: Mapped[str] = mapped_column(String(45), nullable=True)
    user_agent: Mapped[str] = mapped_column(String(500), nullable=True)
