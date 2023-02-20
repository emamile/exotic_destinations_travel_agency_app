from typing import Optional

from pydantic import UUID4, BaseModel

from app.users.schemas.user_schema import UserSchema


class TravelerSchema(BaseModel):
    id: UUID4
    name: str
    surname: str
    telephone_number: str
    passport_number: str
    user_id: str
    user: UserSchema

    class Config:
        orm_mode = True


class TravelerSchemaIn(BaseModel):
    name: str
    surname: str
    telephone_number: str
    passport_number: str
    user_id: str

    class Config:
        orm_mode = True


class TravelerSchemaUpdate(BaseModel):
    id: str
    name: Optional[str] = None
    surname: Optional[str] = None
    telephone_number: Optional[str] = None
    passport_number: Optional[str] = None

    class Config:
        orm_mode = True
