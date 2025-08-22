"""
Database configuration and connection management
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.config import settings
from typing import AsyncGenerator

# Async engine for FastAPI
engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URI.replace("postgresql://", "postgresql+asyncpg://"),
    echo=settings.DEBUG,
    future=True,
    poolclass=StaticPool,
    connect_args={
        "check_same_thread": False,
    } if settings.SQLALCHEMY_DATABASE_URI.startswith("sqlite") else {},
)

# Async session factory
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Base class for models
Base = declarative_base()

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for getting async database session"""
    async with AsyncSessionLocal() as session:
        yield session

async def init_db():
    """Initialize database and create tables"""
    async with engine.begin() as conn:
        # Import all models here to ensure they are registered with SQLAlchemy
        from app.models import user, conversation, message, tulpa, tulpa_memory  # noqa

        await conn.run_sync(Base.metadata.create_all)

async def drop_db():
    """Drop all tables (useful for testing)"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
