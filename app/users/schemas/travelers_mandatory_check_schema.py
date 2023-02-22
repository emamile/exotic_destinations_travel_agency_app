# Importing the UUID4 and BaseModel classes from the pydantic library.
from pydantic import UUID4, BaseModel

from app.users.schemas.travelers_booked_arrangement_schema import BookedArrangementSchema
from app.world_destinations.schemas.state_info_schema import StateInfoSchema


# This class is used to validate the input data for the TravelersMandatoryCheck API.
class TravelersMandatoryCheckSchema(BaseModel):
    id: UUID4
    is_fulfilled: bool
    booked_arrangement_id: str
    state_info_id: str
    booked_arrangement: BookedArrangementSchema
    state_info: StateInfoSchema

    class Config:
        orm_mode = True


# This class is used to validate the input data for the TravelersMandatoryCheck API.
class TravelersMandatoryCheckSchemaIn(BaseModel):
    is_fulfilled: bool
    booked_arrangement_id: str
    state_info_id: str

    class Config:
        orm_mode = True


# This class is used to update the TravelersMandatoryCheckSchema model.
class TravelersMandatoryCheckSchemaUpdate(BaseModel):
    check_id: str
    is_fulfilled: bool

    class Config:
        orm_mode = True
