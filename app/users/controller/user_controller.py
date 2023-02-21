from fastapi import HTTPException, Response
from pydantic import EmailStr
from sqlalchemy.exc import IntegrityError

from app.users.exceptions import UserAlreadyExistsException, UserInvalidPasswordException, UserNotFoundException
from app.users.services import UserService, sign_jwt


class UserController:
    @staticmethod
    def create_user(email: EmailStr, password: str):
        try:
            user = UserService.create_user(email=email, password=password)
            return user
        except UserAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_super_user(email: EmailStr, password: str):
        try:
            user = UserService.create_super_user(email=email, password=password)
            return user
        except UserAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_users():
        try:
            users = UserService.get_all_users()
            return users
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_user_by_id(user_id: str):
        try:
            user = UserService.get_user_by_id(user_id=user_id)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_user_by_email(email: EmailStr):
        try:
            user = UserService.get_user_by_email(email=email)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_users_email_and_password(user_id: str, email: EmailStr, password: str):
        try:
            user = UserService.get_user_by_id(user_id=user_id)
            user = UserService.update_users_email_and_password(user_id=user_id, email=email, password=password)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_user_by_id(user_id: str):
        try:
            if UserService.delete_user_by_id(user_id=user_id):
                return Response(content=f"User with provided ID {user_id} is deleted.", status_code=200)
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def login_user(email: EmailStr, password: str):
        try:
            user = UserService.login_user(email=email, password=password)
            if user.is_superuser:
                return sign_jwt(user.id, "superuser")
            return sign_jwt(user.id, "user")
        except UserInvalidPasswordException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
