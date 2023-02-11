from pydantic import UUID4, BaseModel

from app.world_destinations.schemas.world_destination_schema import WorldDestinationSchema


class StateSchema(BaseModel):
    id: UUID4
    name: str
    basic_info: str
    world_destination_id: str
    world_destination: WorldDestinationSchema

    class Config:
        orm_mode = True


class StateSchemaIn(BaseModel):
    name: str
    basic_info: str
    world_destination_id: str

    class Config:
        orm_mode = True


class StateSchemaUpdate(BaseModel):
    id: str
    basic_info: str

    class Config:
        orm_mode = True
