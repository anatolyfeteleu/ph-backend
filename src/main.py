from fastapi import FastAPI
from src.reference.routers import router as reference_router
from src.organization.routers import router as organization_router


app = FastAPI(title="Paw Hugs", debug=True)

# Register routers

app.include_router(
    router=reference_router,
    prefix="/references",
)
app.include_router(
    router=organization_router,
    prefix="/organizations"
)
