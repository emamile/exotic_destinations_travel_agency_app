from uuid import uuid4

from sqlalchemy import Column, String

from app.database.db import Base


class WorldDestination(Base):
    __tablename__ = "world_destinations"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50), unique=True, nullable=False)

    def __init__(self, name: str):
        self.name = name
