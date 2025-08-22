"""
User model for authentication and user management
"""
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=True)
    hashed_password = Column(String, nullable=True)
    preferences = Column(String, nullable=True)  # JSON string of user preferences
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    conversations = relationship("Conversation", back_populates="user")
    tulpas = relationship("Tulpa", back_populates="user")
