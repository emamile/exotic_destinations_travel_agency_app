from pydantic import BaseModel, UUID4
from app.arrangements.schemas.arrangement_schema import ArrangementSchema
from app.users.schemas.traveler_schema import TravelerSchema


class BookedArrangementSchema(BaseModel):
    id: UUID4
    arrangement_id: str
    traveler_id: str
    arrangement: ArrangementSchema
    traveler: TravelerSchema

    class Config:
        orm_mode = True


class BookedArrangementSchemaIn(BaseModel):
    arrangement_id: str
    traveler_id: str

    class Config:
        orm_mode = True
