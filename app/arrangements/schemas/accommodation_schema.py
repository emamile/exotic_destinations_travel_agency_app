from pydantic import UUID4, BaseModel


# The AccommodationSchema class inherits from the BaseModel class and has the following attributes:
#
# - id
# - name
# - description
# - location
# - price
# - image_url
# - owner_id
# - created_at
# - updated_at
class AccommodationSchema(BaseModel):
    id: UUID4
    name: str
    type: str
    description: str

    class Config:
        orm_mode = True


# A class that defines the schema for the accommodation model.
class AccommodationSchemaIn(BaseModel):
    name: str
    type: str
    description: str

    class Config:
        orm_mode = True


# > This class is used to update an accommodation
class AccommodationSchemaUpdate(BaseModel):
    id: str
    description: str

    class Config:
        orm_mode = True
