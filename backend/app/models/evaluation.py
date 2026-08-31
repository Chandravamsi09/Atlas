from sqlalchemy import String, Boolean, ForeignKey, JSON, Integer, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.db.base import Base


class EvaluationDataset(Base):
    __tablename__ = "evaluation_datasets"

    org_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    samples: Mapped[list] = mapped_column(JSON, default=list, nullable=False) # [{input, ground_truth, metadata}]

    runs = relationship("EvaluationRun", back_populates="dataset", cascade="all, delete-orphan")


class EvaluationRun(Base):
    __tablename__ = "evaluation_runs"

    dataset_id: Mapped[str] = mapped_column(String(36), ForeignKey("evaluation_datasets.id", ondelete="CASCADE"), nullable=False, index=True)
    model_name: Mapped[str] = mapped_column(String(100), nullable=False)
    prompt_version_id: Mapped[str] = mapped_column(String(36), nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="pending", nullable=False)
    aggregate_scores: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False) # {faithfulness, relevance, bertscore, bleu}

    dataset = relationship("EvaluationDataset", back_populates="runs")
    results = relationship("EvaluationResult", back_populates="run", cascade="all, delete-orphan")


class EvaluationResult(Base):
    __tablename__ = "evaluation_results"

    run_id: Mapped[str] = mapped_column(String(36), ForeignKey("evaluation_runs.id", ondelete="CASCADE"), nullable=False, index=True)
    sample_index: Mapped[int] = mapped_column(Integer, nullable=False)
    model_output: Mapped[str] = mapped_column(Text, nullable=False)
    scores: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
    reasoning: Mapped[str] = mapped_column(Text, nullable=True)

    run = relationship("EvaluationRun", back_populates="results")
