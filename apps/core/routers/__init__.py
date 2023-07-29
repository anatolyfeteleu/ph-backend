from apps.core.routers.views import router as hello_router

from utils.api.routers import TypedAPIRouter

hello_router = TypedAPIRouter(
    router=hello_router,
    prefix="/hello",
    tags=["hello"]
)
