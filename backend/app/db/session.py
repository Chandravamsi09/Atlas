from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from backend.app.core.config import settings

# Determine connection URL with SQLite fallback for local developer workstations
db_url = settings.DATABASE_URL
sync_url = settings.SYNC_DATABASE_URL

try:
    if "postgresql+asyncpg" in db_url:
        import asyncpg
except Exception:
    db_url = "sqlite+aiosqlite:///./atlas_local.db"
    sync_url = "sqlite:///./atlas_local.db"

try:
    async_engine = create_async_engine(
        db_url,
        echo=settings.DEBUG,
        pool_pre_ping=True
    )
except Exception:
    async_engine = create_async_engine("sqlite+aiosqlite:///./atlas_local.db")

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

try:
    sync_engine = create_engine(sync_url, echo=settings.DEBUG, pool_pre_ping=True)
except Exception:
    sync_engine = create_engine("sqlite:///./atlas_local.db")

SyncSessionLocal = sessionmaker(
    bind=sync_engine,
    autocommit=False,
    autoflush=False
)


async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
