from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.extensions.dependencies import get_async_session
from src.reference import services
from src.reference.serializers import (
    ServiceSerializer, CitySerializer
)

router = APIRouter()


@router.get(
    "/cities",
    description="List of cities",
    response_description="Return list of cities",
    response_model=List[CitySerializer]
)
async def get_cities(session: AsyncSession = Depends(get_async_session)):

    return await services.get_cities(session)


@router.get(
    "/services",
    description="List of services",
    response_description="Return list of services",
    response_model=List[ServiceSerializer]
)
async def get_services(session: AsyncSession = Depends(get_async_session)):

    return await services.get_services(session)
