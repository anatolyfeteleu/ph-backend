from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.extensions.dependencies import get_async_session
from src.organization import services
from src.organization.serializers import OrganizationSerializer, BranchSerializer

router = APIRouter()


@router.get(
    "/",
    description="List of organizations",
    response_description="Return list of organizations",
    response_model=List[OrganizationSerializer],
    deprecated=True
)
async def get_organizations(session: AsyncSession = Depends(get_async_session)):

    return await services.get_organizations(session)


@router.get(
    "/branches",
    description="List of organizations branches",
    response_description="Return list of organizations branches",
    response_model=List[BranchSerializer],
)
async def get_branches(session: AsyncSession = Depends(get_async_session)):

    return await services.get_branches(session)
