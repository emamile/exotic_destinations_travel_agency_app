from uuid import uuid4

from sqlalchemy import Column, String, UniqueConstraint

from app.database.db import Base


# The Accommodation class is a subclass of the Base class. It has a constructor that takes in a name, price, and rating.
# It also has a method called __str__ that returns a string representation of the object.
class Accommodation(Base):
    __tablename__ = "accommodations"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50), nullable=False)
    type = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)

    __table_args__ = (UniqueConstraint("name", "type", "description", name="accommodation_uc"),)

    def __init__(self, name: str, type: str, description: str):
        self.name = name
        self.type = type
        self.description = description
