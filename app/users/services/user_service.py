import hashlib
from http import HTTPStatus

from pydantic import EmailStr
from sqlalchemy.exc import IntegrityError

from app.database.db import SessionLocal
from app.users.exceptions import UserInvalidPasswordException, UserNotFoundException, UserAlreadyExistsException
from app.users.repository import UserRepository


class UserService:
    @staticmethod
    def create_user(email: EmailStr, password: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(email=email, password=hashed_password)
        except IntegrityError:
            raise UserAlreadyExistsException(code=HTTPStatus.BAD_REQUEST, message=f"User with email {email} already exists.")
        except Exception as e:
            raise e

    @staticmethod
    def create_super_user(email: EmailStr, password: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_super_user(email=email, password=hashed_password)
        except IntegrityError:
            raise UserAlreadyExistsException(code=HTTPStatus.BAD_REQUEST, message=f"Super user with email {email} already exists.")
        except Exception as e:
            raise e

    @staticmethod
    def get_all_users():
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                users = user_repository.get_all_users()
                if users:
                    return users
                raise UserNotFoundException(code=400, message="Currently, there are no users existing.")
        except Exception as e:
            raise e

    @staticmethod
    def get_user_by_id(user_id: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                user = user_repository.get_user_by_id(user_id=user_id)
                if user:
                    return user
                raise UserNotFoundException(message=f"User with provided ID {user_id} does not exist.", code=400)
        except Exception as e:
            raise e

    @staticmethod
    def get_user_by_email(email: EmailStr):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                user = user_repository.get_user_by_email(email=email)
                if user:
                    return user
                raise UserNotFoundException(message=f"User with provided email {email} does not exist.", code=400)
        except Exception as e:
            raise e

    @staticmethod
    def update_users_email_and_password(user_id: str, email: EmailStr, password: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                user1 = user_repository.get_user_by_email(email=email)
                if user1:
                    raise UserAlreadyExistsException(message=f"User with provided email {email} already exists.", code=400)
                user = user_repository.update_users_email_and_password(user_id=user_id, email=email, password=password)
                return user
        except Exception as e:
            raise e

    @staticmethod
    def delete_user_by_id(user_id: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                if user_repository.delete_user_by_id(user_id=user_id):
                    return True
                else:
                    raise UserNotFoundException(message=f"User with provided ID {user_id} does not exist.", code=400)
        except Exception as e:
            raise e

    @staticmethod
    def login_user(email: EmailStr, password: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                user = user_repository.get_user_by_email(email=email)
                if hashlib.sha256(bytes(password, "uft-8")).hexdigest() != user.password:
                    raise UserInvalidPasswordException(message="Invalid password.", code=401)
                else:
                    return user
        except Exception as e:
            raise e
