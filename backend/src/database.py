from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from backend.src.settings import DATA_BASE_URL

async_engine = create_async_engine(DATA_BASE_URL)
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
