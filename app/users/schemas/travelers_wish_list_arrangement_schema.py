# Importing the BaseModel class from the pydantic library.
from pydantic import BaseModel

from app.arrangements.schemas.arrangement_schema import ArrangementSchema
from app.users.schemas.traveler_schema import TravelerSchema


# A class that inherits from the BaseModel class.
class WishListForArrangementsSchema(BaseModel):
    arrangement_id: str
    traveler_id: str
    arrangement: ArrangementSchema
    traveler: TravelerSchema

    class Config:
        orm_mode = True


# A class that defines the schema for the input data.
class WishListForArrangementsSchemaIn(BaseModel):
    arrangement_id: str
    traveler_id: str

    class Config:
        orm_mode = True
