from fastapi import HTTPException, Response
from pydantic import EmailStr

from app.users.exceptions import UserAlreadyExistsException, UserInvalidPasswordException, UserNotFoundException
from app.users.services import EmailService, UserService, sign_jwt


# > This class is responsible for handling user related requests
class UserController:
    @staticmethod
    def create_user(email: EmailStr, password: str):
        """
        > It creates a user

        :param email: EmailStr - This is a custom type that we created in the schemas.py file. It's a string that is
        validated to be a valid email address
        :type email: EmailStr
        :param password: str
        :type password: str
        :return: The user object
        """
        try:
            user = UserService.create_user(email=email, password=password)
            return user
        except UserAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def create_super_user(email: EmailStr, password: str):
        """
        > Create a super user with the given email and password

        :param email: EmailStr - This is a custom type that we created in the models.py file. It's a string that is
        validated to be a valid email address
        :type email: EmailStr
        :param password: str
        :type password: str
        :return: The user object is being returned.
        """
        try:
            user = UserService.create_super_user(email=email, password=password)
            return user
        except UserAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_users():
        """
        It gets all users
        :return: A list of all users
        """
        try:
            users = UserService.get_all_users()
            return users
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_user_by_id(user_id: str):
        """
        > This function gets a user by id

        :param user_id: The user id of the user we want to get
        :type user_id: str
        :return: A user object
        """
        try:
            user = UserService.get_user_by_id(user_id=user_id)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_user_by_email(email: EmailStr):
        """
        > This function gets a user by email

        :param email: EmailStr
        :type email: EmailStr
        :return: A user object
        """
        try:
            user = UserService.get_user_by_email(email=email)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def update_users_email_and_password(user_id: str, email: EmailStr, password: str):
        """
        It updates the user's email and password.

        :param user_id: str - The user's id
        :type user_id: str
        :param email: EmailStr
        :type email: EmailStr
        :param password: str
        :type password: str
        :return: The user object is being returned.
        """
        try:
            user = UserService.get_user_by_id(user_id=user_id)
            user = UserService.update_users_email_and_password(user_id=user_id, email=email, password=password)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except UserAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_user_by_id(user_id: str):
        """
        It deletes a user by ID.

        :param user_id: str - the ID of the user to be deleted
        :type user_id: str
        :return: Response object
        """
        try:
            if UserService.delete_user_by_id(user_id=user_id):
                return Response(content=f"User with provided ID {user_id} is deleted.", status_code=200)
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def login_user(email: EmailStr, password: str):
        """
        > This function logs in a user and sends an email to the user if the login is successful

        :param email: EmailStr - This is a custom type that we created in the models.py file. It's a string that has to be a
        valid email address
        :type email: EmailStr
        :param password: str
        :type password: str
        :return: A JWT token
        """
        try:
            user = UserService.login_user(email=email, password=password)
            if user.is_superuser:
                return sign_jwt(user.id, "superuser")
            return sign_jwt(user.id, "user")
        except UserInvalidPasswordException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
