# Importing the EmailStr class from the pydantic library.
from pydantic import EmailStr
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.models import User


# This class is responsible for retrieving users from the database.
class UserRepository:
    def __init__(self, database: Session):
        self.database = database

    def create_user(self, email: EmailStr, password: str):
        """
        It creates a user with the given email and password, and returns the user

        :param email: EmailStr
        :type email: EmailStr
        :param password: str
        :type password: str
        :return: The user object is being returned.
        """
        try:
            user = User(email=email, password=password)
            self.database.add(user)
            self.database.commit()
            self.database.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def create_super_user(self, email: EmailStr, password: str):
        """
        It creates a super user

        :param email: EmailStr, password: str
        :type email: EmailStr
        :param password: str
        :type password: str
        :return: The user object
        """
        try:
            user = User(email=email, password=password, is_superuser=True)
            self.database.add(user)
            self.database.commit()
            self.database.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def get_all_users(self):
        """
        It gets all the users from the database
        :return: A list of all the users in the database.
        """
        try:
            users = self.database.query(User).all()
            return users
        except Exception as e:
            raise e

    def get_user_by_id(self, user_id: str):
        """
        It gets a user from the database by their id

        :param user_id: The user's ID
        :type user_id: str
        :return: A user object
        """
        try:
            user = self.database.query(User).filter(User.id == user_id).first()
            return user
        except Exception as e:
            raise e

    def get_user_by_email(self, email: EmailStr):
        """
        It takes an email address as a parameter, queries the database for a user with that email address, and returns the
        user if found

        :param email: EmailStr
        :type email: EmailStr
        :return: A user object
        """
        try:
            user = self.database.query(User).filter(User.email == email).first()
            return user
        except Exception as e:
            raise e

    def update_users_email_and_password(self, user_id: str, email: EmailStr = None, password: str = None):
        """
        It updates the email and password of a user in the database

        :param user_id: str
        :type user_id: str
        :param email: EmailStr = None
        :type email: EmailStr
        :param password: str = None
        :type password: str
        :return: The user object is being returned.
        """
        try:
            user = self.database.query(User).filter(User.id == user_id).first()
            if email is not None:
                user.email = email
            if password is not None:
                user.password = password
            self.database.add(user)
            self.database.commit()
            self.database.refresh(user)
            return user
        except Exception as e:
            raise e

    def delete_user_by_id(self, user_id: str):
        """
        It deletes a user from the database by their id

        :param user_id: The id of the user to delete
        :type user_id: str
        :return: A boolean value.
        """
        try:
            user = self.database.query(User).filter(User.id == user_id).first()
            if user is None:
                return False
            self.database.delete(user)
            self.database.commit()
            return True
        except Exception as e:
            raise e
