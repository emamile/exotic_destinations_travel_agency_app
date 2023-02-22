# A type hint. It is used to tell the IDE that the variable is optional.
from typing import Optional

from pydantic import UUID4, BaseModel

from app.users.schemas.user_schema import UserSchema

# The TravelerSchema class inherits from the BaseModel class, which is a class that comes from the Marshmallow library.
#
# The TravelerSchema class is a class that will be used to serialize and deserialize data.
#
# The TravelerSchema class has a class attribute called class Meta, which is a dictionary that contains a key called
# model, which is set to the Traveler class.
#
# The TravelerSchema class has a class attribute called fields, which is a tuple that contains the names of the fields
# that will be serialized and deserialized.
#
# The TravelerSchema class has a class attribute called dump_only, which is a tuple that contains the names of the fields
# that will only be serialized.
#
# The TravelerSchema class has a class attribute called load_only, which is a tuple that contains the names of the fields
# that will only be deserialized


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


# This class is used to validate the input data for the Traveler model.
class TravelerSchemaIn(BaseModel):
    name: str
    surname: str
    telephone_number: str
    passport_number: str
    user_id: str

    class Config:
        orm_mode = True


# This class is used to update the traveler's information.
class TravelerSchemaUpdate(BaseModel):
    id: str
    name: Optional[str] = None
    surname: Optional[str] = None
    telephone_number: Optional[str] = None
    passport_number: Optional[str] = None

    class Config:
        orm_mode = True
