# Importing the uuid4 function from the uuid module.
from uuid import uuid4

from sqlalchemy import Boolean, Column, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.database.db import Base


# > The StateInfo class is a table in the database that stores information about the states.
class StateInfo(Base):
    __tablename__ = "state_informations"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    info_title = Column(String(500), nullable=False)
    details = Column(String(2000), nullable=False)
    is_mandatory = Column(Boolean, nullable=True)

    state_id = Column(String(50), ForeignKey("states.id"))
    state = relationship("State", lazy="subquery")

    __table_args__ = (UniqueConstraint("info_title", "state_id", name="info_uc"),)

    def __init__(self, info_title: str, details: str, is_mandatory: bool, state_id: str):
        self.is_mandatory = is_mandatory
        self.info_title = info_title
        self.details = details
        self.state_id = state_id
