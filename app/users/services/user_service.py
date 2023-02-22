# It's importing the hashlib library.
import hashlib

from pydantic import EmailStr
from sqlalchemy.exc import IntegrityError

from app.database.db import SessionLocal
from app.users.exceptions import UserAlreadyExistsException, UserInvalidPasswordException, UserNotFoundException
from app.users.repository import UserRepository


# > This class provides a service for managing users
class UserService:
    @staticmethod
    def create_user(email: EmailStr, password: str):
        """
        "Create a user with the given email and password."

        The function takes two arguments: email and password. The email argument is of type EmailStr, which is a type
        defined in the pydantic library. The password argument is of type str

        :param email: EmailStr - This is a custom type that we created in the `types.py` file. It's a string that is
        validated to be a valid email address
        :type email: EmailStr
        :param password: str
        :type password: str
        :return: The user object
        """
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(email=email, password=hashed_password)
        except IntegrityError as exc:
            raise UserAlreadyExistsException(code=409, message=f"User with email {email} already exists.") from exc
        except Exception as e:
            raise e

    @staticmethod
    def create_super_user(email: EmailStr, password: str):
        """
        > It creates a super user with the given email and password

        :param email: EmailStr - This is a custom type that we created in the models.py file. It's a string that is
        validated to be a valid email address
        :type email: EmailStr
        :param password: str
        :type password: str
        :return: The user object
        """
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_super_user(email=email, password=hashed_password)
        except IntegrityError as exc:
            raise UserAlreadyExistsException(code=409, message=f"Super user with email {email} already exists.") from exc
        except Exception as e:
            raise e

    @staticmethod
    def get_all_users():
        """
        It gets all the users from the database
        :return: A list of all users in the database.
        """
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
        """
        It gets a user by ID

        :param user_id: The ID of the user you want to get
        :type user_id: str
        :return: A user object
        """
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
        """
        It gets a user by email

        :param email: EmailStr - this is a custom type that we created in the types.py file. It's a string that is validated
        to be a valid email address
        :type email: EmailStr
        :return: User object
        """
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
        """
        It updates the user's email and password

        :param user_id: str
        :type user_id: str
        :param email: EmailStr
        :type email: EmailStr
        :param password: str
        :type password: str
        :return: User object
        """
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
        """
        It deletes a user from the database by their ID

        :param user_id: str
        :type user_id: str
        :return: A boolean value.
        """
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                if user_repository.delete_user_by_id(user_id=user_id):
                    return True
                raise UserNotFoundException(message=f"User with provided ID {user_id} does not exist.", code=400)
        except Exception as e:
            raise e

    @staticmethod
    def login_user(email: EmailStr, password: str):
        """
        > This function takes an email and password, and returns a user object if the password is correct

        :param email: EmailStr - This is a custom type that we created in the types.py file. It's a string that has to be a
        valid email address
        :type email: EmailStr
        :param password: str
        :type password: str
        :return: A user object.
        """
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                user = user_repository.get_user_by_email(email=email)
                if hashlib.sha256(bytes(password, "utf-8")).hexdigest() != user.password:
                    raise UserInvalidPasswordException(message="Invalid password.", code=401)
                return user
        except Exception as e:
            raise e
