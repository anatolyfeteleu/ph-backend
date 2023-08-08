from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.config import SETTINGS

REDIS_URL = (
    f"redis://"
    f"{SETTINGS.REDIS_HOSTNAME}:{SETTINGS.REDIS_PORT}"
    f"/{SETTINGS.REDIS_DB}"
)

DATABASE_URL = (
    f"postgresql+asyncpg://"
    f"{SETTINGS.DB_USERNAME}:{SETTINGS.DB_PASSWORD}"
    f"@{SETTINGS.DB_HOSTNAME}"
    f"/{SETTINGS.DB_NAME}"
)


Base = declarative_base()

async_engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(  # NOQA
    async_engine, class_=AsyncSession, expire_on_commit=False
)
