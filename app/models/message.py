"""
Message model for storing individual chat messages
"""
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Float, func
from sqlalchemy.orm import relationship

from app.core.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"), nullable=False)
    role = Column(String, nullable=False)  # 'user', 'assistant', 'system'
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    metadata = Column(String, nullable=True)  # JSON string for additional data
    tokens_used = Column(Integer, nullable=True)
    model_used = Column(String, nullable=True)

    # Relationships
    conversation = relationship("Conversation", back_populates="messages")
