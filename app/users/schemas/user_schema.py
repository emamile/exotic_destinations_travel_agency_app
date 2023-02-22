# Importing the UUID4, BaseModel, and EmailStr classes from the pydantic module.
from pydantic import UUID4, BaseModel, EmailStr


# > This class is a schema for the User model
class UserSchema(BaseModel):
    id: UUID4
    email: EmailStr
    password: str
    is_superuser: bool

    class Config:
        orm_mode = True


# A class that inherits from the BaseModel class.
class UserSchemaIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


# A class that inherits from the BaseModel class.
class UserSchemaUpdate(BaseModel):
    id: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
