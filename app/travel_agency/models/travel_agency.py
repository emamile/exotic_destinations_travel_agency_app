from uuid import uuid4

from sqlalchemy import Column, String

from app.database import Base


class TravelAgency(Base):
    __tablename__ = "travel_agency"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    email = Column(String(100), unique=True)
    password = Column(String(100))
    address = Column(String(100))
    telephone_number = Column(String(30))

    def __init__(self, name, email, password, address, telephone_number):
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.telephone_number = telephone_number
