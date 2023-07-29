from typing import TYPE_CHECKING

import aioredis

from project.settings.database import REDIS_URL

if TYPE_CHECKING:
    from aioredis import Redis


def configure_redis() -> "Redis":
    return aioredis.from_url(
        REDIS_URL,
        decode_responses=True,
        encoding="utf8",
    )
