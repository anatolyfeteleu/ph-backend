from fastapi import FastAPI
from fastapi_pagination import add_pagination

from src.reference.routers import router as reference_router
from src.organization.routers import router as organization_router


app = FastAPI(title="Paw Hugs", debug=True)

app.include_router(
    router=reference_router,
    prefix="/references",
)
app.include_router(
    router=organization_router,
    prefix="/organizations"
)

add_pagination(app)
