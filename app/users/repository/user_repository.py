from pydantic import EmailStr
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.models import User


class UserRepository:
    def __init__(self, database: Session):
        self.database = database

    def create_user(self, email: EmailStr, password: str):
        try:
            user = User(email=email, password=password)
            self.database.add(user)
            self.database.commit()
            self.database.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def create_super_user(self, email: EmailStr, password: str):
        try:
            user = User(email=email, password=password, is_superuser=True)
            self.database.add(user)
            self.database.commit()
            self.database.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def get_all_users(self):
        users = self.database.query(User).all()
        return users

    def get_user_by_id(self, user_id: str):
        user = self.database.query(User).filter(User.id == user_id).first()
        return user

    def get_user_by_email(self, email: EmailStr):
        user = self.database.query(User).filter(User.email == email).first()
        return user

    def update_user_email_and_password(self, user_id: str, email: EmailStr, password: str):
        try:
            user = self.database.query(User).filter(User.id == user_id).first()
            user.email = email
            user.password = password
            self.database.add(user)
            self.database.commit()
            self.database.refresh(user)
            return user
        except Exception as e:
            raise e

    def delete_user_by_id(self, user_id: str):
        try:
            user = self.database.query(User).filter(User.id == user_id).first()
            if user is None:
                return False
            self.database.delete(user)
            self.database.commit()
            return True
        except Exception as e:
            raise e
