from typing import Optional

from pydantic import UUID4, BaseModel

from app.arrangements.schemas import AccommodationSchema, ArrangementSchema, ExcursionSchema


# > This class is a schema for the PlanAndProgramPerDay model
class PlanAndProgramPerDaySchema(BaseModel):
    id: UUID4
    title: str
    location: str
    description: str
    food: Optional[str] = None
    excursion_id: Optional[str] = None
    accommodation_id: Optional[str] = None
    arrangement_id: str
    excursion: Optional[ExcursionSchema] = None
    accommodation: Optional[AccommodationSchema] = None
    arrangement: ArrangementSchema

    class Config:
        orm_mode = True


# A class that inherits from the BaseModel class.
class PlanAndProgramPerDaySchemaIn(BaseModel):
    title: str
    location: str
    description: str
    food: Optional[str] = None
    excursion_id: Optional[str] = None
    accommodation_id: Optional[str] = None
    arrangement_id: str

    class Config:
        orm_mode = True


# > This class is used to update the plan and program per day schema
class PlanAndProgramPerDaySchemaUpdate(BaseModel):
    id: str
    title: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    food: Optional[str] = None
    excursion_id: Optional[str] = None
    accommodation_id: Optional[str] = None

    class Config:
        orm_mode = True
