from typing import Optional

from pydantic import BaseModel, UUID4
from app.arrangements.schemas import ExcursionSchema, AccommodationSchema, ArrangementSchema


class PlanAndProgramPerDaySchema(BaseModel):
    id: UUID4
    title: str
    location: str
    description: str
    food: Optional[str] = None
    excursion_id: Optional[str] = None
    accommodation_id: Optional[str] = None
    arrangement_id: str
    excursion: ExcursionSchema = None
    accommodation: AccommodationSchema = None
    arrangement: ArrangementSchema

    class Config:
        orm_mode = True


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
