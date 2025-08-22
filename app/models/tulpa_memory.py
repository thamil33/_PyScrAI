"""
TulpaMemory model for storing AI companion memories
Note: This is designed for extensibility - room for dynamic memory system expansion
"""
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Float, JSON, func
from sqlalchemy.orm import relationship

from app.core.database import Base


class TulpaMemory(Base):
    __tablename__ = "tulpa_memories"

    id = Column(Integer, primary_key=True, index=True)
    tulpa_id = Column(Integer, ForeignKey("tulpas.id"), nullable=False)
    content = Column(Text, nullable=False)
    memory_type = Column(String, nullable=False)  # 'experience', 'knowledge', 'preference', etc.
    importance_score = Column(Float, default=0.5)  # 0.0 to 1.0
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    access_count = Column(Integer, default=0)
    last_accessed = Column(DateTime(timezone=True), nullable=True)

    # Extensible fields for future memory system enhancements
    metadata = Column(JSON, nullable=True)  # For flexible metadata storage
    embedding = Column(JSON, nullable=True)  # For vector embeddings if needed
    tags = Column(JSON, nullable=True)  # For categorization and searchability

    # Relationships
    tulpa = relationship("Tulpa", back_populates="memories")
