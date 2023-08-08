from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.reference.models import City, Service


async def get_cities(session: AsyncSession) -> List[City]:

    result = await session.execute(select(City))
    return result.scalars().all()


async def get_services(session: AsyncSession) -> List[Service]:

    result = await session.execute(select(Service))
    return result.scalars().all()
