from typing import Optional, List, TYPE_CHECKING

from sqlalchemy import (
    BigInteger, String, Float, SmallInteger, ForeignKey
)
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database import Base
from src.extensions.models import BaseModelMixin

if TYPE_CHECKING:
    from src.reference.models import WorkDay, City, Service


class Organization(BaseModelMixin, Base):

    __tablename__ = "organization_organization"

    name: Mapped[str] = mapped_column(
        nullable=False,
        info={"verbose_name": "organization name"},
    )
    website: Mapped[Optional[str]] = mapped_column(
        nullable=True,
        info={"verbose_name": "website"},
    )

    branches: Mapped[List["Branch"]] = relationship(
        back_populates="organization"
    )


class Branch(BaseModelMixin, Base):

    __tablename__ = "organization_branch"

    organization_id = mapped_column(
        ForeignKey("organization_organization.id"), nullable=False,
        info={"verbose_name": "organization"}
    )
    city_id: Mapped[int] = mapped_column(
        ForeignKey("reference_city.id"), nullable=False,
        info={"verbose_name": "city"}
    )
    email: Mapped[str] = mapped_column(
        String(320),
        nullable=False,
        info={"verbose_name": "email"},
    )
    phone: Mapped[str] = mapped_column(
        String(18), nullable=False,
        info={"verbose_name": "phone"},
    )
    street: Mapped[str] = mapped_column(
        String(128), nullable=False,
        info={"verbose_name": "street"},
    )
    latitude: Mapped[float] = mapped_column(
        Float(precision=6),
        info={"verbose_name": "latitude"}
    )
    longitude: Mapped[float] = mapped_column(
        Float(precision=6),
        info={"verbose_name": "longitude"}
    )

    organization: Mapped["Organization"] = relationship(
        back_populates="branches"
    )
    city: Mapped["City"] = relationship(
        back_populates="branches"
    )
    opening_hours: Mapped[List["BranchOpeningHours"]] = relationship(
        back_populates="branches"
    )
    services: Mapped[List["BranchService"]] = relationship(
        back_populates="branch"
    )


class BranchOpeningHours(BaseModelMixin, Base):

    __tablename__ = "organization_branchopeninghours"

    branch_id: Mapped[int] = mapped_column(
        ForeignKey("organization_branch.id"), nullable=False,
        info={"verbose_name": "branch"}
    )
    work_day_id: Mapped[int] = mapped_column(
        ForeignKey("reference_workday.id"), nullable=False,
        info={"verbose_name": "work day"}
    )
    time_from: Mapped[int] = mapped_column(
        SmallInteger(),
        info={"verbose_name": "time from"}
    )
    time_to: Mapped[int] = mapped_column(
        SmallInteger(),
        info={"verbose_name": "time to"}
    )

    branches: Mapped["Branch"] = relationship(
        back_populates="opening_hours"
    )
    work_day: Mapped["WorkDay"] = relationship(
        back_populates="opening_hours"
    )


class BranchService(Base):

    __tablename__ = "organization_branchservice"

    branch_id: Mapped[int] = mapped_column(
        ForeignKey("organization_branch.id"), primary_key=True,
        info={"verbose_name": "branch"}
    )
    service_id: Mapped[int] = mapped_column(
        ForeignKey("reference_service.id"), primary_key=True,
        info={"verbose_name": "service"}
    )

    branch: Mapped["Branch"] = relationship(
        back_populates="services"
    )
    service: Mapped["Service"] = relationship(
        back_populates="branch_services"
    )

