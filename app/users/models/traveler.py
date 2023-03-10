from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database.db import Base


# The Traveler class is a subclass of the Base class. It has a constructor that takes in a name, a location, and a list of
# destinations. It also has a method called get_traveler_location that returns the location of the traveler.
class Traveler(Base):
    __tablename__ = "travelers"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    telephone_number = Column(String(50), nullable=False)
    passport_number = Column(String(20), unique=True, nullable=False)

    user_id = Column(String(50), ForeignKey("users.id"))
    user = relationship("User", lazy="subquery", uselist=False)

    def __init__(self, name: str, surname: str, telephone_number: str, passport_number: str, user_id: str):
        self.name = name
        self.surname = surname
        self.telephone_number = telephone_number
        self.passport_number = passport_number
        self.user_id = user_id

    def __eq__(self, other):
        if self.id != other.id:
            return False
        if self.name != other.name:
            return False
        if self.surname != other.surname:
            return False
        if self.telephone_number != other.telephone_number:
            return False
        if self.passport_number != other.passport_number:
            return False
        if self.user_id != other.user_id:
            return False
        return True

    def __ne__(self, other):
        if self.id == other.id:
            return False
        if self.name == other.name:
            return False
        if self.surname == other.surname:
            return False
        if self.telephone_number == other.telephone_number:
            return False
        if self.passport_number == other.passport_number:
            return False
        if self.user_id == other.user_id:
            return False
        return True
