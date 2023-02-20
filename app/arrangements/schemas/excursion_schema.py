from pydantic import BaseModel, UUID4
from typing import Optional


class ExcursionSchema(BaseModel):
    id: UUID4
    name: str
    price: float
    description: str

    class Config:
        orm_mode = True


class ExcursionSchemaIn(BaseModel):
    name: str
    price: float
    description: str

    class Config:
        orm_mode = True


class ExcursionSchemaUpdate(BaseModel):
    id: str
    price: Optional[float]
    description: Optional[str]

    class Config:
        orm_mode = True
