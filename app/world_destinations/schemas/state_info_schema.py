# A type hint. It is telling the IDE that the variable is optional.
from typing import Optional

from pydantic import UUID4, BaseModel

from app.world_destinations.schemas.state_schema import StateSchema


# > This class is a data model for the state information of a single state
class StateInfoSchema(BaseModel):
    id: UUID4
    info_title: str
    details: str
    is_mandatory: Optional[bool] = None
    state_id: str
    state: StateSchema

    class Config:
        orm_mode = True


# > This class is used to deserialize the request body of the `/state_info` endpoint
class StateInfoSchemaIn(BaseModel):
    info_title: str
    details: str
    is_mandatory: Optional[bool] = None
    state_id: str

    class Config:
        orm_mode = True


# > This class is used to update the state info schema
class StateInfoSchemaUpdate(BaseModel):
    id: str
    details: Optional[str] = None
    is_mandatory: Optional[bool] = None

    class Config:
        orm_mode = True


# class UsefulInfoAboutStateSchemaUpdate(BaseModel):
#     visa_info: Optional[str] = None
#     is_visa_needed: Optional[bool] = None
#     vaccine_info: Optional[str] = None
#     is_vaccine_needed: Optional[bool] = None
#     safety: Optional[str] = None
#     money: Optional[str] = None
#     insurance: Optional[str] = None
#     time_zone: Optional[str] = None
#     electricity_internet_communication: Optional[str] = None
#     food: Optional[str] = None
#     souvenirs: Optional[str] = None
#     other_notes: Optional[str] = None
#     state_id: str
#
#     class Config:
#         orm_mode = True
