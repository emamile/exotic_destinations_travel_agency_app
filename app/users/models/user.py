from uuid import uuid4

from sqlalchemy import Boolean, Column, String

from app.database.db import Base


# > The User class is a subclass of the Base class, and it has a constructor that takes in a first name, last name, and
# email address
class User(Base):
    __tablename__ = "users"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)

    def __init__(self, email: str, password: str, is_superuser=False):
        self.email = email
        self.password = password
        self.is_superuser = is_superuser

    def __eq__(self, other):
        if self.id != other.id:
            return False
        if self.email != other.email:
            return False
        if self.password != other.password:
            return False
        if self.is_superuser != other.is_superuser:
            return False
        return True

    def __ne__(self, other):
        if self.id == other.id:
            return False
        if self.email == other.email:
            return False
        if self.password == other.password:
            return False
        if self.is_superuser == other.is_superuser:
            return False
        return True
