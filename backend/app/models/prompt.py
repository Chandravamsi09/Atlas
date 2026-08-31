from sqlalchemy import String, Boolean, ForeignKey, JSON, Integer, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.db.base import Base


class PromptTemplate(Base):
    __tablename__ = "prompt_templates"

    org_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    tags: Mapped[list] = mapped_column(JSON, default=list, nullable=False)
    active_version_id: Mapped[str] = mapped_column(String(36), nullable=True)

    organization = relationship("Organization", back_populates="prompts")
    versions = relationship("PromptVersion", back_populates="template", cascade="all, delete-orphan")
    experiments = relationship("PromptExperiment", back_populates="template", cascade="all, delete-orphan")


class PromptVersion(Base):
    __tablename__ = "prompt_versions"

    template_id: Mapped[str] = mapped_column(String(36), ForeignKey("prompt_templates.id", ondelete="CASCADE"), nullable=False, index=True)
    version_number: Mapped[int] = mapped_column(Integer, nullable=False)
    system_prompt: Mapped[str] = mapped_column(Text, nullable=True)
    user_prompt_template: Mapped[str] = mapped_column(Text, nullable=False) # Jinja2
    input_variables: Mapped[list] = mapped_column(JSON, default=list, nullable=False) # list of {name, type, required}
    model_config_schema: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False) # {model, temperature, max_tokens}
    commit_message: Mapped[str] = mapped_column(String(500), nullable=True)
    author_id: Mapped[str] = mapped_column(String(36), nullable=True)

    template = relationship("PromptTemplate", back_populates="versions")


class PromptExperiment(Base):
    __tablename__ = "prompt_experiments"

    template_id: Mapped[str] = mapped_column(String(36), ForeignKey("prompt_templates.id", ondelete="CASCADE"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    traffic_split: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False) # {version_id: weight_pct}
    status: Mapped[str] = mapped_column(String(50), default="active", nullable=False) # active, paused, concluded
    metrics: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)

    template = relationship("PromptTemplate", back_populates="experiments")
