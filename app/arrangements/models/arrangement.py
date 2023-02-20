from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String, DATE, Integer, Float, Boolean
from sqlalchemy.orm import relationship
from app.database.db import Base


class Arrangement(Base):
    __tablename__ = "arrangements"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(100), nullable=False)
    code = Column(String(10), unique=True, nullable=False)
    date_of_departure = Column(DATE, nullable=False)
    date_of_arrival = Column(DATE, nullable=False)
    duration = Column(Integer, nullable=False)
    description = Column(String(1000), nullable=False)
    air_route_to_the_destination = Column(String(1000), nullable=False)
    price = Column(Float, nullable=False)
    demandingness = Column(Integer, nullable=False)
    availability = Column(Boolean, default=True)
    included_in_price = Column(String(1000), nullable=False)
    not_included_in_price = Column(String(1000), nullable=False)

    state_id = Column(String(50), ForeignKey("states.id"))
    state = relationship("State", lazy="subquery")

    def __init__(self, name: str, code: str, date_of_departure: str, date_of_arrival: str,
                 duration: int, description: str, air_route_to_the_destination: str,
                 price: float, demandingness: int, availability: bool, included_in_price: str,
                 not_included_in_price: str, state_id: str):
        self.name = name
        self.code = code
        self.date_of_departure = datetime.strptime(date_of_departure, "%Y-%m-%d")
        self.date_of_arrival = datetime.strptime(date_of_arrival, "%Y-%m-%d")
        self.duration = duration
        self.description = description
        self.air_route_to_the_destination = air_route_to_the_destination
        self.price = price
        self.demandingness = demandingness
        self.availability = availability
        self.included_in_price = included_in_price
        self.not_included_in_price = not_included_in_price
        self.state_id = state_id
