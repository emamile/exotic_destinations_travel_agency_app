from pydantic import UUID4, BaseModel, EmailStr


class TravelAgencySchema(BaseModel):
    id: UUID4
    name: str
    email: str
    password: str
    address: str
    telephone_number: str

    class Config:
        orm_mode = True


class TravelAgencySchemaIn(BaseModel):
    name: str
    email: EmailStr
    password: str
    address: str
    telephone_number: str

    class Config:
        orm_mode = True
