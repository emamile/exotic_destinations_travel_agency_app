import hashlib

from pydantic import EmailStr

from app.database.db import SessionLocal
from app.users.exceptions import UserInvalidPasswordException
from app.users.repository import UserRepository


class UserService:
    @staticmethod
    def create_user(email: EmailStr, password: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(email=email, password=hashed_password)
            except Exception as e:
                raise e

    @staticmethod
    def create_super_user(email: EmailStr, password: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_super_user(email=email, password=hashed_password)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_users():
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.get_all_users()
            except Exception as e:
                raise e

    @staticmethod
    def get_user_by_id(user_id):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.get_user_by_id(user_id=user_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_user_by_email(email: EmailStr):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.get_user_by_email(email=email)
            except Exception as e:
                raise e

    @staticmethod
    def update_user_email_and_password(user_id: str, email: EmailStr, password: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.update_user_email_and_password(user_id=user_id, email=email, password=password)
            except Exception as e:
                raise e

    @staticmethod
    def delete_user_by_id(user_id: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                if user_repository.delete_user_by_id(user_id=user_id):
                    return True
                else:
                    return False
            except Exception as e:
                raise e

    @staticmethod
    def login_user(email: EmailStr, password: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user = user_repository.get_user_by_email(email=email)
                if hashlib.sha256(bytes(password, "uft-8")).hexdigest() != user.password:
                    raise UserInvalidPasswordException(message="Invalid password.", code=401)
                else:
                    return user
            except Exception as e:
                raise e
