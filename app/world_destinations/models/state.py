from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database.db import Base


class State(Base):
    __tablename__ = "states"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50), unique=True, nullable=False)
    basic_info = Column(String(1000), nullable=False)

    world_destination_id = Column(String(50), ForeignKey("world_destinations.id"))
    world_destination = relationship("WorldDestination", lazy="subquery")

    def __init__(self, name: str, basic_info: str, world_destination_id: str):
        self.name = name
        self.basic_info = basic_info
        self.world_destination_id = world_destination_id
