# Importing the UUID4 and BaseModel classes from the pydantic library.
from pydantic import UUID4, BaseModel

from app.world_destinations.schemas.world_destination_schema import WorldDestinationSchema


# > This class is a schema for the State model
class StateSchema(BaseModel):
    id: UUID4
    name: str
    basic_info: str
    world_destination_id: str
    world_destination: WorldDestinationSchema

    class Config:
        orm_mode = True


# > This class is used to validate the input data for the `/state` endpoint
class StateSchemaIn(BaseModel):
    name: str
    basic_info: str
    world_destination_id: str

    class Config:
        orm_mode = True


# > This class is used to update the state schema
class StateSchemaUpdate(BaseModel):
    id: str
    basic_info: str

    class Config:
        orm_mode = True
