from uuid import uuid4

from sqlalchemy import Column, Float, String, UniqueConstraint

from app.database.db import Base


# > The Excursion class is a subclass of the Base class
class Excursion(Base):
    __tablename__ = "excursions"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(500), nullable=False)

    __table_args__ = (UniqueConstraint("name", "price", "description", name="oe_uc"),)

    def __init__(self, name: str, price: float, description: str):
        self.name = name
        self.price = price
        self.description = description
