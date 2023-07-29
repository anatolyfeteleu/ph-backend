from pydantic import Field
from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    DB_NAME: str
    DB_USERNAME: str
    DB_HOSTNAME: str
    DB_PORT: str
    DB_PASSWORD: str


class RedisSettings(BaseSettings):
    REDIS_HOSTNAME: str
    REDIS_PORT: str
    REDIS_DB: str


DATABASE_SETTINGS = DatabaseSettings(
    _env_file=".env",
    _env_file_encoding="utf-8"
)
REDIS_SETTINGS = RedisSettings(
    _env_file=".env",
    _env_file_encoding="utf-8"
)
