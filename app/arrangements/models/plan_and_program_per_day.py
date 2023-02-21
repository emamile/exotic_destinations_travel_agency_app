from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database.db import Base


class PlanAndProgramPerDay(Base):
    __tablename__ = "plan_and_program_per_day"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    title = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    description = Column(String(1000), nullable=False)
    food = Column(String(500), nullable=False)

    excursion_id = Column(String(50), ForeignKey("excursions.id"))
    excursion = relationship("Excursion", lazy="subquery")

    accommodation_id = Column(String(50), ForeignKey("accommodations.id"))
    accommodation = relationship("Accommodation", lazy="subquery")

    arrangement_id = Column(String(50), ForeignKey("arrangements.id"))
    arrangement = relationship("Arrangement", lazy="subquery")

    __table_args__ = (UniqueConstraint("title", "arrangement_id", name="p_and_p_uc"),)

    def __init__(self, title: str, location: str, description: str, food: str, excursion_id: str,
                 accommodation_id: str, arrangement_id: str):
        self.title = title
        self.location = location
        self.description = description
        self.food = food
        self.excursion_id = excursion_id
        self.accommodation_id = accommodation_id
        self.arrangement_id = arrangement_id

