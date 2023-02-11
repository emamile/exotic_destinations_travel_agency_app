from uuid import uuid4

from sqlalchemy import Boolean, Column, String

from app.database.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    is_superuser = Column(Boolean, default=False)

    def __init__(self, email: str, password: str, is_superuser=False):
        self.email = email
        self.password = password
        self.is_superuser = is_superuser
