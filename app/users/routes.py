from fastapi import APIRouter, Depends
from pydantic import EmailStr

from app.users.controller import UserController
from app.users.controller.user_auth_handler_controller import JWTBearer
from app.users.schemas.user_schema import UserSchema, UserSchemaIn

user_router = APIRouter(tags=["USERS"], prefix="/api/users")


@user_router.post("/add-user", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create_user(email=user.email, password=user.password)


@user_router.post("/add-superuser", response_model=UserSchema)
def create_super_user(user: UserSchemaIn):
    return UserController.create_super_user(email=user.email, password=user.password)


@user_router.post("/login")
def login_user(user: UserSchemaIn):
    return UserController.login_user(email=user.email, password=user.password)


@user_router.get("/get-all-users", response_model=list[UserSchema])
def get_all_users():
    return UserController.get_all_users()


@user_router.get("/get-user-by-id", response_model=UserSchema)
def get_user_by_id(user_id: str):
    return UserController.get_user_by_id(user_id)


@user_router.get("/get-user-by-email", response_model=UserSchema)
def get_user_by_email(email: EmailStr):
    return UserController.get_user_by_email(email=email)


@user_router.put("/update/email-and-password", response_model=UserSchema)
def update_user(user_id: str, email: EmailStr, password: str):
    return UserController.update_user_email_and_password(user_id=user_id, email=email, password=password)


@user_router.delete("/delete-user-by-id")
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)
