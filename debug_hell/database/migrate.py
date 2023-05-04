import asyncio

from debug_hell.database.models import Base
from debug_hell.database.session import engine


async def migrate() -> None:
    """Migrate database tables."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(migrate())
