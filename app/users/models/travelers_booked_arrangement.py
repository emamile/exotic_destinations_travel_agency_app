from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database.db import Base


# > A BookedArrangement is a booking of a specific arrangement for a specific date
class BookedArrangement(Base):
    __tablename__ = "travelers_booked_arrangements"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)

    arrangement_id = Column(String(50), ForeignKey("arrangements.id"))
    arrangement = relationship("Arrangement", lazy="subquery")

    traveler_id = Column(String(50), ForeignKey("travelers.id"))
    traveler = relationship("Traveler", lazy="subquery")

    def __init__(self, arrangement_id: str, traveler_id: str):
        self.arrangement_id = arrangement_id
        self.traveler_id = traveler_id
