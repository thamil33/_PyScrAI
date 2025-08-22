"""
Tulpa model for AI companion personalities
"""
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Float, func
from sqlalchemy.orm import relationship

from app.core.database import Base


class Tulpa(Base):
    __tablename__ = "tulpas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    personality_traits = Column(Text, nullable=True)  # JSON string of personality traits
    backstory = Column(Text, nullable=True)
    provider = Column(String, nullable=True)
    model_used = Column(String, nullable=True)
    system_prompt = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="tulpas")
    memories = relationship("TulpaMemory", back_populates="tulpa")
