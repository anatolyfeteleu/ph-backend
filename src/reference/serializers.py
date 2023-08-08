from pydantic import BaseModel, ConfigDict, constr


class CitySerializer(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class WorkDaySerializer(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    short_name: str


class ServiceSerializer(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
