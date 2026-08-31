from sqlalchemy import String, Boolean, ForeignKey, JSON, Integer, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.db.base import Base


class KnowledgeBase(Base):
    __tablename__ = "knowledge_bases"

    org_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    embedding_model: Mapped[str] = mapped_column(String(100), default="text-embedding-3-small", nullable=False)
    dimension: Mapped[int] = mapped_column(Integer, default=1536, nullable=False)
    chunking_strategy: Mapped[str] = mapped_column(String(50), default="recursive", nullable=False)
    chunk_size: Mapped[int] = mapped_column(Integer, default=512, nullable=False)
    chunk_overlap: Mapped[int] = mapped_column(Integer, default=64, nullable=False)

    organization = relationship("Organization", back_populates="knowledge_bases")
    chunks = relationship("DocumentChunk", back_populates="knowledge_base", cascade="all, delete-orphan")


class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    knowledge_base_id: Mapped[str] = mapped_column(String(36), ForeignKey("knowledge_bases.id", ondelete="CASCADE"), nullable=False, index=True)
    document_title: Mapped[str] = mapped_column(String(500), nullable=False)
    document_uri: Mapped[str] = mapped_column(String(1024), nullable=True)
    chunk_index: Mapped[int] = mapped_column(Integer, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    metadata_fields: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
    token_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    embedding_vector: Mapped[list] = mapped_column(JSON, default=list, nullable=True)

    knowledge_base = relationship("KnowledgeBase", back_populates="chunks")
