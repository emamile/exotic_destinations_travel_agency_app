# Importing the UUID4 and BaseModel classes from the pydantic module.
from pydantic import UUID4, BaseModel

from app.arrangements.schemas.arrangement_schema import ArrangementSchema
from app.users.schemas.traveler_schema import TravelerSchema


# This class is a model for the BookedArrangement table in the database
class BookedArrangementSchema(BaseModel):
    id: UUID4
    arrangement_id: str
    traveler_id: str
    arrangement: ArrangementSchema
    traveler: TravelerSchema

    class Config:
        orm_mode = True


# A class that inherits from the BaseModel class.
class BookedArrangementSchemaIn(BaseModel):
    arrangement_id: str
    traveler_id: str

    class Config:
        orm_mode = True
