from fastapi import APIRouter, Depends
from pydantic import EmailStr

from app.users.controller.user_controller import UserController
from app.users.controller.traveler_controller import TravelerController
from app.users.controller.travelers_booked_arrangement_controller import BookedArrangementController
from app.users.controller.travelers_wish_list_arrangement_controller import WishListForArrangementsController
from app.users.controller.traveler_obligation_checker_controller import TravelerObligationCheckerController
from app.users.controller.user_auth_handler_controller import JWTBearer
from app.users.schemas.user_schema import UserSchema, UserSchemaIn
from app.users.schemas.traveler_schema import TravelerSchema, TravelerSchemaIn, TravelerSchemaUpdate
from app.users.schemas.travelers_booked_arrangement_schema import BookedArrangementSchema, BookedArrangementSchemaIn
from app.users.schemas.travelers_wish_list_arrangement_schema import WishListForArrangementsSchema, WishListForArrangementsSchemaIn
from app.users.schemas.traveler_obligation_checker_schema import TravelerObligationCheckerSchema, TravelerObligationCheckerSchemaIn


user_router = APIRouter(tags=["USERS"], prefix="/api/users")
traveler_router = APIRouter(tags=["TRAVELERS"], prefix="/api/travelers")


@user_router.post("/add-user", response_model=UserSchema)
def add_user(user: UserSchemaIn):
    return UserController.create_user(email=user.email, password=user.password)


@user_router.post("/add-superuser", response_model=UserSchema)
def add_super_user(user: UserSchemaIn):
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
    return UserController.update_users_email_and_password(user_id=user_id, email=email, password=password)


@user_router.delete("/delete-user-by-id")
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)


@traveler_router.post("/add-traveler", response_model=TravelerSchema)
def add_traveler(traveler: TravelerSchemaIn):
    return TravelerController.create_traveler(name=traveler.name, surname=traveler.surname, telephone_number=traveler.telephone_number, passport_number=traveler.passport_number, user_id=traveler.user_id)


@traveler_router.get("/get-all-travelers", response_model=list[TravelerSchema])
def get_all_travelers():
    return TravelerController.get_all_travelers()


@traveler_router.get("/get-traveler-by-id", response_model=TravelerSchema)
def get_traveler_by_id(traveler_id: str):
    return TravelerController.get_traveler_by_id(traveler_id=traveler_id)


@traveler_router.get("/get-traveler-by-passport-number", response_model=TravelerSchema)
def get_traveler_by_passport_number(passport_number: str):
    return TravelerController.get_traveler_by_passport_number(passport_number=passport_number)


@traveler_router.put("/update-traveler's-info", response_model=TravelerSchema)
def update_traveler(traveler: TravelerSchemaUpdate):
    return TravelerController.update_traveler(traveler_id=traveler.id, surname=traveler.surname, telephone_number=traveler.telephone_number, passport_number=traveler.passport_number)


@traveler_router.delete("/delete-traveler-by-id")
def delete_traveler_by_id(traveler_id: str):
    return TravelerController.delete_traveler_by_id(traveler_id=traveler_id)


@traveler_router.post("/book-arrangement-for-traveler", response_model=BookedArrangementSchema)
def book_arrangement_for_traveler(booked_arrangement: BookedArrangementSchemaIn):
    return BookedArrangementController.create_travelers_booked_arrangement(arrangement_id=booked_arrangement.arrangement_id, traveler_id=booked_arrangement.traveler_id)


@traveler_router.get("/get-traveler's-booked-arrangements", response_model=list[BookedArrangementSchema])
def get_travelers_booked_arrangements(traveler_id: str):
    return BookedArrangementController.get_travelers_booked_arrangements(traveler_id=traveler_id)


@traveler_router.delete("/delete-traveler's-booked-arrangements")
def delete_travelers_booked_arrangement(arrangement_id: str, traveler_id):
    return BookedArrangementController.delete_travelers_booked_arrangement(arrangement_id=arrangement_id, traveler_id=traveler_id)


@traveler_router.post("/add-arrangement-to-travelers-wish-list", response_model=WishListForArrangementsSchema)
def add_arrangement_to_travelers_wish_list(wish_list_arrangement: WishListForArrangementsSchemaIn):
    return WishListForArrangementsController.create_travelers_wish_list_arrangement(arrangement_id=wish_list_arrangement.arrangement_id, traveler_id=wish_list_arrangement.traveler_id)


@traveler_router.get("/get-traveler's-wish-list-arrangements", response_model=list[WishListForArrangementsSchema])
def get_travelers_wish_list_arrangements(traveler_id: str):
    return WishListForArrangementsController.get_travelers_wish_list_arrangements(traveler_id=traveler_id)


@traveler_router.delete("/delete-traveler's-arrangement-from-wish-list")
def delete_travelers_arrangement_from_wish_list(arrangement_id: str, traveler_id: str):
    return WishListForArrangementsController.delete_travelers_wish_list_arrangement(arrangement_id=arrangement_id, traveler_id=traveler_id)


@traveler_router.post("/create-checkers-for-travelers-booked-arrangements")
def create_checkers_for_booked_arrangements():
    return TravelerObligationCheckerController.create_checkers_for_booked_arrangements()


@traveler_router.get("/get-all-existing-checkers")
def get_all_existing_checkers():
    return TravelerObligationCheckerController.get_all_existing_checkers()


@traveler_router.get("/get-all-checkers-for-arrangement")
def get_checkers_for_arrangement(arrangement_id: str):
    return TravelerObligationCheckerController.get_checkers_for_arrangement(arrangement_id=arrangement_id)


@traveler_router.get("/get-all-checkers-that-belong-to-traveler")
def get_all_checkers_that_belong_to_traveler(traveler_id: str):
    return TravelerObligationCheckerController.get_all_checkers_that_belong_to_traveler(traveler_id=traveler_id)


@traveler_router.get("/get-all-travelers-that-have-all-checkers-valid")
def get_all_travelers_that_have_all_checkers_valid():
    return TravelerObligationCheckerController.get_all_travelers_that_have_all_checkers_valid()


@traveler_router.get("/get-all-travelers-that-do-not-have-all-checkers-valid")
def get_all_travelers_that_do_not_have_all_checkers_valid():
    return TravelerObligationCheckerController.get_all_travelers_that_do_not_have_all_checkers_valid()


@traveler_router.put("/update-travelers-checker-for-booked-arrangement")
def update_travelers_checker_for_arrangement(checker: TravelerObligationCheckerSchemaIn):
    return TravelerObligationCheckerController.update_travelers_checker_for_arrangement(arrangement_id=checker.arrangement_id, traveler_id=checker.traveler_id, is_passport_valid=checker.is_passport_valid, is_visa_valid=checker.is_visa_valid, is_vaccine_received=checker.is_vaccine_received)


@traveler_router.delete("/delete-checker-for-traveler-and-arrangement")
def delete_checker_for_traveler_and_arrangement(arrangement_id: str, traveler_id: str):
    return TravelerObligationCheckerController.delete_checker_for_traveler_and_arrangement(arrangement_id=arrangement_id, traveler_id=traveler_id)

