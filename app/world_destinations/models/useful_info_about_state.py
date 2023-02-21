from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship

from app.database.db import Base


class UsefulInfoAboutState(Base):
    __tablename__ = "useful_info_about_state"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    info_title = Column(String(500), nullable=False)
    details = Column(String(2000), nullable=False)
    is_visa_needed = Column(Boolean, nullable=True)
    is_vaccine_needed = Column(Boolean, nullable=True)
    is_insurance_needed = Column(Boolean, nullable=True)
    
    state_id = Column(String(50), ForeignKey("states.id"))
    state = relationship("State", lazy="subquery")

    __table_args__ = (UniqueConstraint("info_title", "state_id", name="info_uc"),)
    
    def __init__(self, info_title: str, details: str, state_id: str):
        self.info_title = info_title
        self.details = details
        if info_title == "visa":
            self.is_visa_needed = False
        if info_title == "vaccine":
            self.is_vaccine_needed = False
        if info_title == "insurance":
            self.is_insurance_needed = False
        self.state_id = state_id
        