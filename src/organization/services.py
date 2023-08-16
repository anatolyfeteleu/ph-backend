from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from src.organization.models import (
    Organization, Branch, BranchOpeningHours, BranchService
)


async def get_organizations(session: AsyncSession) -> Sequence[Organization]:

    result = await session.execute(
        select(Organization)
        .options(
            selectinload(Organization.branches)
            .selectinload(Branch.opening_hours)
            .selectinload(BranchOpeningHours.work_day)
        )
    )
    scalars = result.scalars().all()
    return scalars


async def get_branches(session: AsyncSession) -> Sequence[Branch]:

    query = (
        select(Branch)

        .options(
            joinedload(Branch.city),
            joinedload(Branch.organization),
            (
                joinedload(Branch.opening_hours)
                .joinedload(BranchOpeningHours.work_day)
            ),
            (
                joinedload(Branch.services)
                .joinedload(BranchService.service)
            )
        )
        .order_by(Branch.created)
    )
    result = await session.execute(query)
    scalars = result.unique().scalars().all()
    return scalars
