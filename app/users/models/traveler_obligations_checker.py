from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship

from app.database.db import Base


class TravelerObligationsChecker(Base):

    __tablename__ = "traveler_obligations_checkers"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    is_passport_valid = Column(Boolean, default=False, nullable=False)
    is_visa_valid = Column(Boolean, default=False)
    is_vaccine_received = Column(Boolean, default=False)

    arrangement_id = Column(String(50), ForeignKey("arrangements.id"))
    arrangement = relationship("Arrangement", lazy="subquery")

    traveler_id = Column(String(50), ForeignKey("travelers.id"))
    traveler = relationship("Traveler", lazy="subquery")
    __table_args__ = (UniqueConstraint("arrangement_id", "traveler_id", name="checker_uc"),)

    def __init__(self, is_passport_valid: bool, is_visa_valid: bool, is_vaccine_received: bool, arrangement_id: str, traveler_id: str):
        self.is_passport_valid = is_passport_valid
        self.is_visa_valid = is_visa_valid
        self.is_vaccine_received = is_vaccine_received
        self.arrangement_id = arrangement_id
        self.traveler_id = traveler_id
