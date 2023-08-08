from typing import List

from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
from src.organization.models import Branch


class WorkDay(Base):

    __tablename__ = "reference_workday"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(
        String(11), nullable=False,
        info={"verbose_name": "name"}
    )
    short_name: Mapped[str] = mapped_column(
        String(4), nullable=False,
        info={"verbose_name": "short name"}
    )

    opening_hours: Mapped["BranchOpeningHours"] = relationship(
        back_populates="work_day"
    )


class City(Base):

    __tablename__ = "reference_city"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(
        String(32), nullable=False,
        info={"verbose_name": "city name"}
    )

    branches: Mapped[List["Branch"]] = relationship(
        back_populates="city"
    )


class Service(Base):

    __tablename__ = "reference_service"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(
        String(32),
        info={"verbose_name": "name"}
    )
