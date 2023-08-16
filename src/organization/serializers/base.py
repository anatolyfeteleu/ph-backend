from pydantic import BaseModel, ConfigDict


class BranchOpeningHoursBaseSerializer(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int


class BranchServiceBaseSerializer(BaseModel):

    model_config = ConfigDict(from_attributes=True)


class BranchBaseSerializer(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int


class OrganizationBaseSerializer(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
