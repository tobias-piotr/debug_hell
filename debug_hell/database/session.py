from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from debug_hell.config import settings

engine = create_async_engine(settings.DATABASE_URL)
session_factory = async_sessionmaker(engine)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Get database session."""
    async with session_factory() as session:
        yield session
