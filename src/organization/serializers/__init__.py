from typing import List
from pydantic.fields import Field

from src.organization.serializers.base import (
    BranchBaseSerializer, BranchOpeningHoursBaseSerializer,
    BranchServiceBaseSerializer, OrganizationBaseSerializer
)
from src.reference.serializers import (
    CitySerializer, WorkDaySerializer, ServiceSerializer
)


class BranchOpeningHoursListSerializer(BranchOpeningHoursBaseSerializer):

    time_from: int
    time_to: int

    work_day: WorkDaySerializer


class BranchServiceSerializer(BranchServiceBaseSerializer):

    service: ServiceSerializer


class OrganizationShortSerializer(OrganizationBaseSerializer):

    name: str


class BranchListSerializer(BranchBaseSerializer):

    email: str
    phone: str
    street: str
    latitude: float
    longitude: float

    organization: OrganizationShortSerializer
    city: CitySerializer
    opening_hours: List[BranchOpeningHoursListSerializer]
    services: List[BranchServiceSerializer]