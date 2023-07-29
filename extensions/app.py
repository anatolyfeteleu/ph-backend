from inspect import getmembers

from fastapi import FastAPI

from utils.api.routers import TypedAPIRouter

__all__ = (
    "init",
)


def init(app: "FastAPI"):
    """
    Init routers and etc.
    :return:
    """
    init_routers(app)


def init_routers(app: "FastAPI"):
    """
    Initialize routers defined in `app.api`
    :param app:
    :return:
    """
    from apps.core import routers

    routers = [
        o[1]
        for o in getmembers(routers)
        if isinstance(o[1], TypedAPIRouter)
    ]

    for router in routers:
        app.include_router(**router.dict())
