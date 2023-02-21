from pydantic import BaseModel, UUID4
from typing import Optional
from app.world_destinations.schemas.state_schema import StateSchema


class UsefulInfoAboutStateSchema(BaseModel):
    id: UUID4
    info_title: str
    details: str
    is_visa_needed: Optional[bool] = None
    is_vaccine_needed: Optional[bool] = None
    is_insurance_needed: Optional[bool] = None
    state_id: str
    state: StateSchema

    class Config:
        orm_mode = True


class UsefulInfoAboutStateSchemaIn(BaseModel):
    info_title: str
    details: str
    state_id: str

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
