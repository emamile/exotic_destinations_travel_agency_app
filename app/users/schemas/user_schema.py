from pydantic import BaseModel, UUID4, EmailStr


class UserSchema(BaseModel):
    id: UUID4
    email: str
    password: str
    is_superuser: bool

    class Config:
        orm_mode = True


class UserSchemaIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
