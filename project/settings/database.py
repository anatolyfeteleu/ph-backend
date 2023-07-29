from tortoise import Tortoise

from project.settings import (
    DATABASE_SETTINGS,
    REDIS_SETTINGS
)


REDIS_URL = (
    f"redis://"
    f"{REDIS_SETTINGS.REDIS_HOSTNAME}:{REDIS_SETTINGS.REDIS_PORT}"
    f"/{REDIS_SETTINGS.REDIS_DB}"
)

DATABASE_URL = (
    f"postgres://"
    f"{DATABASE_SETTINGS.DB_USERNAME}:{DATABASE_SETTINGS.DB_PASSWORD}"
    f"@{DATABASE_SETTINGS.DB_HOSTNAME}"
    f"/{DATABASE_SETTINGS.NAME}"
)

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


Tortoise.init_models(models_paths=["models"], app_label="models")
