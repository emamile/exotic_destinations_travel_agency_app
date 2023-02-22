# Importing the uuid4 function from the uuid module.
from uuid import uuid4

from sqlalchemy import Column, String

from app.database.db import Base


# > This class is a representation of a World Destination
class WorldDestination(Base):
    __tablename__ = "world_destinations"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50), unique=True, nullable=False)

    def __init__(self, name: str):
        self.name = name
