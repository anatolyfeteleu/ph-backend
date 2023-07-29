from typing import TYPE_CHECKING

from tortoise.contrib.fastapi import register_tortoise

from project.settings.database import TORTOISE_ORM

if TYPE_CHECKING:
    from fastapi import FastAPI


def init_db(app: "FastAPI") -> None:
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        modules={"models": ["models", "aerich.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
