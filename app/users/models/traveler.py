from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database.db import Base


class Traveler(Base):
    __tablename__ = "travelers"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    telephone_number = Column(String(50), nullable=False)
    passport_number = Column(String(20), unique=True, nullable=False)

    user_id = Column(String(50), ForeignKey("users.id"))
    user = relationship("User", lazy="subquery")

    def __init__(self, name: str, surname: str, telephone_number: str, passport_number: str, user_id: str):
        self.name = name
        self.surname = surname
        self.telephone_number = telephone_number
        self.passport_number = passport_number
        self.user_id = user_id
