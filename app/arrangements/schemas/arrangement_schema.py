from datetime import date
from typing import Optional

from pydantic import UUID4, BaseModel, PositiveFloat, PositiveInt

from app.world_destinations.schemas.state_schema import StateSchema


# > This class is a schema for the Arrangement model
class ArrangementSchema(BaseModel):
    id: UUID4
    name: str
    code: str
    date_of_departure: date
    date_of_arrival: date
    duration: PositiveInt
    description: str
    air_route_to_the_destination: str
    price: PositiveFloat
    demandingness: int
    availability: bool
    included_in_price: str
    not_included_in_price: str
    state_id: str
    state: StateSchema

    class Config:
        orm_mode = True


# > This class is used to validate the input data for the `/arrangements` endpoint
class ArrangementSchemaIn(BaseModel):
    name: str
    code: str
    date_of_departure: str
    date_of_arrival: str
    duration: PositiveInt
    description: str
    air_route_to_the_destination: str
    price: PositiveFloat
    demandingness: int
    availability: bool
    included_in_price: str
    not_included_in_price: str
    state_id: str

    class Config:
        orm_mode = True


# > This class is used to update an arrangement
class ArrangementSchemaUpdate(BaseModel):
    id: str
    price: Optional[PositiveFloat] = None
    availability: Optional[bool] = None

    class Config:
        orm_mode = True
