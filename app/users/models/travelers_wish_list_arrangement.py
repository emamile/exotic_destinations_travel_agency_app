from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database.db import Base


# This class is a table that stores the wish list of arrangements for a user.
class WishListForArrangements(Base):
    __tablename__ = "travelers_wish_list"

    arrangement_id = Column(String(50), ForeignKey("arrangements.id"), primary_key=True)
    arrangement = relationship("Arrangement", lazy="subquery")

    traveler_id = Column(String(50), ForeignKey("travelers.id"))
    traveler = relationship("Traveler", lazy="subquery")

    def __init__(self, arrangement_id: str, traveler_id: str):
        self.arrangement_id = arrangement_id
        self.traveler_id = traveler_id
