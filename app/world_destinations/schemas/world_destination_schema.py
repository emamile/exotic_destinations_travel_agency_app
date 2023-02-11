from pydantic import UUID4, BaseModel


class WorldDestinationSchema(BaseModel):
    id: UUID4
    name: str

    class Config:
        orm_mode = True


class WorldDestinationSchemaIn(BaseModel):
    name: str

    class Config:
        orm_mode = True
