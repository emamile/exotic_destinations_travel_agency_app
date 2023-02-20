from datetime import date
from typing import Optional

from pydantic import BaseModel, UUID4
from app.world_destinations.schemas.state_schema import StateSchema


class ArrangementSchema(BaseModel):
    id: UUID4
    name: str
    code: str
    date_of_departure: date
    date_of_arrival: date
    duration: int
    description: str
    air_route_to_the_destination: str
    price: float
    demandingness: int
    availability: bool
    included_in_price: str
    not_included_in_price: str
    state_id: str
    state: StateSchema

    class Config:
        orm_mode = True


class ArrangementSchemaIn(BaseModel):
    name: str
    code: str
    date_of_departure: str
    date_of_arrival: str
    duration: int
    description: str
    air_route_to_the_destination: str
    price: float
    demandingness: int
    availability: bool
    included_in_price: str
    not_included_in_price: str
    state_id: str

    class Config:
        orm_mode = True


class ArrangementSchemaUpdate(BaseModel):
    id: str
    price: Optional[float] = None
    availability: Optional[bool] = None

    class Config:
        orm_mode = True
