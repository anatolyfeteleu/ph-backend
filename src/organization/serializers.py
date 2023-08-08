from typing import List

from pydantic import BaseModel, ConfigDict, constr

from src.reference.serializers import CitySerializer, WorkDaySerializer


class BranchOpeningHoursSerializer(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    work_day: WorkDaySerializer
    time_from: int
    time_to: int


class BranchServiceSerializer(BaseModel):

    model_config = ConfigDict(from_attributes=True)


class OrganizationSerializer(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    website: str


class BranchSerializer(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    phone: str
    street: str
    latitude: float
    longitude: float

    organization: OrganizationSerializer
    city: CitySerializer
    opening_hours: List[BranchOpeningHoursSerializer]
