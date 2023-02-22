from typing import Optional

from pydantic import UUID4, BaseModel, PositiveFloat


# It creates a class called ExcursionSchema that inherits from BaseModel.
class ExcursionSchema(BaseModel):
    id: UUID4
    name: str
    price: PositiveFloat
    description: str

    class Config:
        orm_mode = True


# This class is used to validate the input data for the excursion endpoints.
class ExcursionSchemaIn(BaseModel):
    name: str
    price: PositiveFloat
    description: str

    class Config:
        orm_mode = True


# > This class is used to update an excursion
class ExcursionSchemaUpdate(BaseModel):
    id: str
    price: Optional[PositiveFloat]
    description: Optional[str]

    class Config:
        orm_mode = True
