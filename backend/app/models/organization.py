from sqlalchemy import String, Boolean, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.db.base import Base


class Organization(Base):
    __tablename__ = "organizations"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    settings: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)

    memberships = relationship("OrgMembership", back_populates="organization", cascade="all, delete-orphan")
    api_keys = relationship("APIKey", back_populates="organization", cascade="all, delete-orphan")
    prompts = relationship("PromptTemplate", back_populates="organization", cascade="all, delete-orphan")
    workflows = relationship("WorkflowDAG", back_populates="organization", cascade="all, delete-orphan")
    knowledge_bases = relationship("KnowledgeBase", back_populates="organization", cascade="all, delete-orphan")
    guardrails = relationship("GuardrailRule", back_populates="organization", cascade="all, delete-orphan")
    quota = relationship("TenantQuota", back_populates="organization", uselist=False, cascade="all, delete-orphan")


class OrgMembership(Base):
    __tablename__ = "org_memberships"

    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    org_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    role: Mapped[str] = mapped_column(String(50), default="engineer", nullable=False) # owner, admin, engineer, analyst, viewer

    user = relationship("User", back_populates="memberships")
    organization = relationship("Organization", back_populates="memberships")
