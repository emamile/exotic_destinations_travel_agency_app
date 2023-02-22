from uuid import uuid4

from sqlalchemy import Boolean, Column, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.database.db import Base


# This class is used to check if the mandatory fields are filled in the Travelers page.
class TravelersMandatoryCheck(Base):
    __tablename__ = "travelers_mandatory_checks"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    is_fulfilled = Column(Boolean, nullable=False, default=False)

    booked_arrangement_id = Column(String(50), ForeignKey("travelers_booked_arrangements.id"))
    booked_arrangement = relationship("BookedArrangement", lazy="subquery")

    state_info_id = Column(String(50), ForeignKey("state_informations.id"))
    state_info = relationship("StateInfo", lazy="subquery")

    __table_args__ = (UniqueConstraint("booked_arrangement_id", "state_info_id", name="check_uc"),)

    def __init__(self, is_fulfilled: bool, booked_arrangement_id: str, state_info_id: str):
        self.is_fulfilled = is_fulfilled
        self.booked_arrangement_id = booked_arrangement_id
        self.state_info_id = state_info_id
