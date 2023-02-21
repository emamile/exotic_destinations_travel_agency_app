from pydantic import BaseModel, UUID4
from app.arrangements.schemas.arrangement_schema import ArrangementSchema
from app.users.schemas.traveler_schema import TravelerSchema
from typing import Optional


class TravelerObligationCheckerSchema(BaseModel):
    id: UUID4
    is_passport_valid: bool
    is_visa_valid: Optional[bool] = None
    is_vaccine_received: Optional[bool] = None
    arrangement_id: str
    traveler_id: str
    arrangement: ArrangementSchema
    traveler: TravelerSchema

    class Config:
        orm_mode = True


class TravelerObligationCheckerSchemaIn(BaseModel):
    is_passport_valid: bool
    is_visa_valid: Optional[bool] = None
    is_vaccine_received: Optional[bool] = None
    arrangement_id: str
    traveler_id: str

    class Config:
        orm_mode = True
