from pydantic import BaseModel, ConfigDict


class CityBaseSerializer(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int


class WorkDayBaseSerializer(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int


class ServiceBaseSerializer(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
