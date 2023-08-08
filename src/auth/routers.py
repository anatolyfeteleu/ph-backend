from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()


@router.get(
    "/get",
    description="Get 'Hello!'",
    response_description="Some text",
    response_class=JSONResponse
)
async def get():
    return JSONResponse(dict(detail="Hello!"))
