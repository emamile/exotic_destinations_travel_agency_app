from pydantic import BaseModel, UUID4


class AccommodationSchema(BaseModel):
    id: UUID4
    name: str
    type: str
    description: str

    class Config:
        orm_mode = True


class AccommodationSchemaIn(BaseModel):
    name: str
    type: str
    description: str

    class Config:
        orm_mode = True


class AccommodationSchemaUpdate(BaseModel):
    id: str
    description: str

    class Config:
        orm_mode = True
