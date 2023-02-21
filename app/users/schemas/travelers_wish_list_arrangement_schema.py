from pydantic import BaseModel
from app.arrangements.schemas.arrangement_schema import ArrangementSchema
from app.users.schemas.traveler_schema import TravelerSchema


class WishListForArrangementsSchema(BaseModel):

    arrangement_id: str
    traveler_id: str
    arrangement: ArrangementSchema
    traveler: TravelerSchema

    class Config:
        orm_mode = True


class WishListForArrangementsSchemaIn(BaseModel):
    arrangement_id: str
    traveler_id: str

    class Config:
        orm_mode = True
