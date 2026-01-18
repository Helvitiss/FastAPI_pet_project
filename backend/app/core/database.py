from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from backend.app.core.config import settings


DATABASE_URL = settings.database_url

class Base(DeclarativeBase):
    pass


async def get_db():
    async with Async_Session() as session:
        yield session




engine = create_async_engine(DATABASE_URL, echo=True)


Async_Session = async_sessionmaker(
    engine,
    expire_on_commit=False,
)