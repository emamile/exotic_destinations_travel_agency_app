from pydantic import UUID4, BaseModel


# > This class is a schema for the WorldDestination model
class WorldDestinationSchema(BaseModel):
    id: UUID4
    name: str

    class Config:
        orm_mode = True


# > This class is used to deserialize the request body of the `/world-destinations` endpoint
class WorldDestinationSchemaIn(BaseModel):
    name: str

    class Config:
        orm_mode = True
