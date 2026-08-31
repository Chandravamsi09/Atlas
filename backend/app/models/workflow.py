from sqlalchemy import String, Boolean, ForeignKey, JSON, Integer, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.db.base import Base


class WorkflowDAG(Base):
    __tablename__ = "workflow_dags"

    org_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    dag_definition: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False) # nodes, edges, state_schema
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    version: Mapped[int] = mapped_column(Integer, default=1, nullable=False)

    organization = relationship("Organization", back_populates="workflows")
    executions = relationship("WorkflowExecution", back_populates="workflow", cascade="all, delete-orphan")


class WorkflowExecution(Base):
    __tablename__ = "workflow_executions"

    workflow_id: Mapped[str] = mapped_column(String(36), ForeignKey("workflow_dags.id", ondelete="CASCADE"), nullable=False, index=True)
    status: Mapped[str] = mapped_column(String(50), default="pending", nullable=False) # pending, running, completed, failed, paused_hitl
    inputs: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
    outputs: Mapped[dict] = mapped_column(JSON, default=dict, nullable=True)
    state_snapshots: Mapped[list] = mapped_column(JSON, default=list, nullable=False)
    total_tokens: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    duration_ms: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    error_message: Mapped[str] = mapped_column(Text, nullable=True)

    workflow = relationship("WorkflowDAG", back_populates="executions")
