from fastapi import APIRouter, Depends
from pydantic import EmailStr

from app.users.controller import TravelerController, TravelersMandatoryCheckController
from app.users.controller.travelers_booked_arrangement_controller import BookedArrangementController
from app.users.controller.travelers_wish_list_arrangement_controller import WishListForArrangementsController
from app.users.controller.user_auth_handler_controller import JWTBearer
from app.users.controller.user_controller import UserController
from app.users.schemas import (
    TravelerSchema,
    TravelerSchemaIn,
    TravelerSchemaUpdate,
    TravelersMandatoryCheckSchema,
    TravelersMandatoryCheckSchemaUpdate,
)
from app.users.schemas.travelers_booked_arrangement_schema import BookedArrangementSchema, BookedArrangementSchemaIn
from app.users.schemas.travelers_wish_list_arrangement_schema import WishListForArrangementsSchema, WishListForArrangementsSchemaIn
from app.users.schemas.user_schema import UserSchema, UserSchemaIn, UserSchemaUpdate

user_router = APIRouter(tags=["USERS"], prefix="/api/users")
traveler_router = APIRouter(tags=["TRAVELERS"], prefix="/api/travelers")
mandatory_check_router = APIRouter(tags=["MANDATORY CHECKS"], prefix="/api/mandatory_checks")


@user_router.post("/add-user", response_model=UserSchema, dependencies=[Depends(JWTBearer("superuser"))])
def add_user(user: UserSchemaIn):
    """
    `add_user` takes a `UserSchemaIn` object and returns a `User` object

    :param user: UserSchemaIn
    :type user: UserSchemaIn
    :return: The return value is a UserSchemaOut object.
    """
    return UserController.create_user(email=user.email, password=user.password)


@user_router.post("/add-superuser", response_model=UserSchema)
def add_super_user(user: UserSchemaIn):
    """
    `add_super_user` creates a super user

    :param user: UserSchemaIn
    :type user: UserSchemaIn
    :return: A user object
    """
    return UserController.create_super_user(email=user.email, password=user.password)


@user_router.post("/login")
def login_user(user: UserSchemaIn):
    """
    `login_user` takes a `UserSchemaIn` object and returns a `UserSchemaOut` object

    :param user: UserSchemaIn - This is the parameter that will be passed to the function
    :type user: UserSchemaIn
    :return: A user object
    """
    return UserController.login_user(email=user.email, password=user.password)


@user_router.get("/get-all-users", response_model=list[UserSchema], dependencies=[Depends(JWTBearer("superuser"))])
def get_all_users():
    """
    `get_all_users()` returns a list of all users
    :return: A list of all users in the database.
    """
    return UserController.get_all_users()


@user_router.get("/get-user-by-id", response_model=UserSchema, dependencies=[Depends(JWTBearer("superuser"))])
def get_user_by_id(user_id: str):
    """
    `get_user_by_id` returns a user object given a user id

    :param user_id: The user's ID
    :type user_id: str
    :return: A user object
    """
    return UserController.get_user_by_id(user_id)


@user_router.get("/get-user-by-email", response_model=UserSchema, dependencies=[Depends(JWTBearer("superuser"))])
def get_user_by_email(email: EmailStr):
    """
    `get_user_by_email` returns a user object given an email address

    :param email: EmailStr
    :type email: EmailStr
    :return: A user object
    """
    return UserController.get_user_by_email(email=email)


@user_router.put("/update/email-and-password", response_model=UserSchema, dependencies=[Depends(JWTBearer("superuser"))])
def update_user(user: UserSchemaUpdate):
    """
    `update_user` updates a user's email and password

    :param user: UserSchemaUpdate
    :type user: UserSchemaUpdate
    :return: The user's email and password are being updated.
    """
    return UserController.update_users_email_and_password(user_id=user.id, email=user.email, password=user.password)


@user_router.delete("/delete-user-by-id", dependencies=[Depends(JWTBearer("superuser"))])
def delete_user_by_id(user_id: str):
    """
    `delete_user_by_id` deletes a user by id

    :param user_id: str
    :type user_id: str
    :return: The return value is the result of the delete_user_by_id function.
    """
    return UserController.delete_user_by_id(user_id)


@mandatory_check_router.get(
    "/get-all-fulfilled-mandatory-checks",
    response_model=list[TravelersMandatoryCheckSchema],
    dependencies=[Depends(JWTBearer("superuser"))],
)
def get_all_fulfilled_mandatory_checks():
    """
    > Returns all fulfilled mandatory checks
    :return: A list of all the fulfilled mandatory checks.
    """
    return TravelersMandatoryCheckController.get_all_fulfilled_mandatory_checks()


@mandatory_check_router.get(
    "/get-all-unfulfilled-mandatory-checks",
    response_model=list[TravelersMandatoryCheckSchema],
    dependencies=[Depends(JWTBearer("superuser"))],
)
def get_all_unfulfilled_mandatory_checks():
    """
    > Get all unfulfilled mandatory checks
    :return: A list of all unfulfilled mandatory checks.
    """
    return TravelersMandatoryCheckController.get_all_unfulfilled_mandatory_checks()


@mandatory_check_router.get(
    "/get-mandatory-check-by-id", response_model=TravelersMandatoryCheckSchema, dependencies=[Depends(JWTBearer("superuser"))]
)
def get_mandatory_check_by_id(check_id: str):
    """
    Get a mandatory check by its ID

    :param check_id: The ID of the check you want to get
    :type check_id: str
    :return: A TravelersMandatoryCheck object
    """
    return TravelersMandatoryCheckController.get_travelers_mandatory_check_by_id(check_id=check_id)


@mandatory_check_router.delete("/delete-mandatory-check-by-id", dependencies=[Depends(JWTBearer("superuser"))])
def delete_mandatory_check_by_id(check_id: str):
    """
    Delete a mandatory check by ID

    :param check_id: The ID of the mandatory check you want to delete
    :type check_id: str
    :return: A boolean value.
    """
    return TravelersMandatoryCheckController.delete_mandatory_check_by_id(check_id=check_id)


@traveler_router.post("/add-traveler", response_model=TravelerSchema, dependencies=[Depends(JWTBearer("superuser"))])
def add_traveler(traveler: TravelerSchemaIn):
    """
    It creates a traveler

    :param traveler: TravelerSchemaIn - this is the input parameter that will be passed to the function
    :type traveler: TravelerSchemaIn
    :return: Traveler object
    """
    return TravelerController.create_traveler(
        name=traveler.name,
        surname=traveler.surname,
        telephone_number=traveler.telephone_number,
        passport_number=traveler.passport_number,
        user_id=traveler.user_id,
    )


@traveler_router.get("/get-all-travelers", response_model=list[TravelerSchema], dependencies=[Depends(JWTBearer("superuser"))])
def get_all_travelers():
    """
    `get_all_travelers()` returns a list of all the travelers in the database
    :return: A list of all the travelers in the database.
    """
    return TravelerController.get_all_travelers()


@traveler_router.get("/get-traveler-by-id", response_model=TravelerSchema, dependencies=[Depends(JWTBearer("superuser"))])
def get_traveler_by_id(traveler_id: str):
    """
    `Get a traveler by their ID.`

    :param traveler_id: str
    :type traveler_id: str
    :return: A traveler object
    """
    return TravelerController.get_traveler_by_id(traveler_id=traveler_id)


@traveler_router.get("/get-traveler-by-passport-number", response_model=TravelerSchema, dependencies=[Depends(JWTBearer("superuser"))])
def get_traveler_by_passport_number(passport_number: str):
    """
    > Get a traveler by passport number

    :param passport_number: str
    :type passport_number: str
    :return: A traveler object
    """
    return TravelerController.get_traveler_by_passport_number(passport_number=passport_number)


@traveler_router.put("/update-traveler's-info", response_model=TravelerSchema, dependencies=[Depends(JWTBearer("superuser"))])
def update_traveler(traveler: TravelerSchemaUpdate):
    """
    `update_traveler` updates a traveler

    :param traveler: TravelerSchemaUpdate - this is the parameter that is passed to the function
    :type traveler: TravelerSchemaUpdate
    :return: The updated traveler.
    """
    return TravelerController.update_traveler(
        traveler_id=traveler.id,
        surname=traveler.surname,
        telephone_number=traveler.telephone_number,
        passport_number=traveler.passport_number,
    )


@traveler_router.delete("/delete-traveler-by-id", dependencies=[Depends(JWTBearer("superuser"))])
def delete_traveler_by_id(traveler_id: str):
    """
    Delete a traveler by id

    :param traveler_id: str
    :type traveler_id: str
    :return: A boolean value.
    """
    return TravelerController.delete_traveler_by_id(traveler_id=traveler_id)


@traveler_router.post("/book-arrangement-for-traveler", response_model=BookedArrangementSchema, dependencies=[Depends(JWTBearer("user"))])
def book_arrangement_for_traveler(booked_arrangement: BookedArrangementSchemaIn):
    """
    > Create a new booked arrangement for a traveler

    :param booked_arrangement: BookedArrangementSchemaIn
    :type booked_arrangement: BookedArrangementSchemaIn
    :return: A BookedArrangementSchemaOut object
    """
    return BookedArrangementController.create_travelers_booked_arrangement(
        arrangement_id=booked_arrangement.arrangement_id, traveler_id=booked_arrangement.traveler_id
    )


@traveler_router.get(
    "/get-traveler's-booked-arrangements", response_model=list[BookedArrangementSchema], dependencies=[Depends(JWTBearer("user"))]
)
def get_travelers_booked_arrangements(traveler_id: str):
    """
    Get all the booked arrangements for a traveler

    :param traveler_id: str
    :type traveler_id: str
    :return: A list of BookedArrangement objects
    """
    return BookedArrangementController.get_travelers_booked_arrangements(traveler_id=traveler_id)


@traveler_router.delete("/delete-traveler's-booked-arrangements", dependencies=[Depends(JWTBearer("user"))])
def delete_travelers_booked_arrangement(arrangement_id: str, traveler_id):
    """
    Delete a traveler's booked arrangement.

    :param arrangement_id: str
    :type arrangement_id: str
    :param traveler_id: The id of the traveler you want to delete from the booked arrangement
    :return: The return value is a dictionary with the key 'message' and the value is a string.
    """
    return BookedArrangementController.delete_travelers_booked_arrangement(arrangement_id=arrangement_id, traveler_id=traveler_id)


@traveler_router.post(
    "/add-arrangement-to-travelers-wish-list", response_model=WishListForArrangementsSchema, dependencies=[Depends(JWTBearer("user"))]
)
def add_arrangement_to_travelers_wish_list(wish_list_arrangement: WishListForArrangementsSchemaIn):
    """
    `add_arrangement_to_travelers_wish_list` adds an arrangement to a traveler's wish list

    :param wish_list_arrangement: WishListForArrangementsSchemaIn
    :type wish_list_arrangement: WishListForArrangementsSchemaIn
    :return: The return value is a WishListForArrangementsSchemaOut object.
    """
    return WishListForArrangementsController.create_travelers_wish_list_arrangement(
        arrangement_id=wish_list_arrangement.arrangement_id, traveler_id=wish_list_arrangement.traveler_id
    )


@traveler_router.get(
    "/get-traveler's-wish-list-arrangements", response_model=list[WishListForArrangementsSchema], dependencies=[Depends(JWTBearer("user"))]
)
def get_travelers_wish_list_arrangements(traveler_id: str):
    """
    Get the wish list of arrangements for a traveler

    :param traveler_id: str
    :type traveler_id: str
    :return: A list of all the arrangements that are in the traveler's wish list.
    """
    return WishListForArrangementsController.get_travelers_wish_list_arrangements(traveler_id=traveler_id)


@traveler_router.delete("/delete-traveler's-arrangement-from-wish-list", dependencies=[Depends(JWTBearer("user"))])
def delete_travelers_arrangement_from_wish_list(arrangement_id: str, traveler_id: str):
    """
    Delete a traveler's wish list arrangement.

    :param arrangement_id: The arrangement id of the arrangement you want to delete from the traveler's wish list
    :type arrangement_id: str
    :param traveler_id: The id of the traveler who's wish list you want to delete the arrangement from
    :type traveler_id: str
    :return: A list of all the arrangements in the wish list of a traveler.
    """
    return WishListForArrangementsController.delete_travelers_wish_list_arrangement(arrangement_id=arrangement_id, traveler_id=traveler_id)


@traveler_router.get("/get-traveler's-mandatory-checks", dependencies=[Depends(JWTBearer("user"))])
def get_travelers_mandatory_checks(traveler_id: str):
    """
    Get the mandatory checks for a traveler

    :param traveler_id: str
    :type traveler_id: str
    :return: A list of TravelersMandatoryCheck objects
    """
    return TravelersMandatoryCheckController.get_travelers_mandatory_checks(traveler_id=traveler_id)


@traveler_router.put(
    "/update-traveler's-mandatory-check", response_model=TravelersMandatoryCheckSchema, dependencies=[Depends(JWTBearer("user"))]
)
def update_travelers_mandatory_check(check: TravelersMandatoryCheckSchemaUpdate):
    """
    `update_travelers_mandatory_check` updates a mandatory check for a traveler

    :param check: TravelersMandatoryCheckSchemaUpdate
    :type check: TravelersMandatoryCheckSchemaUpdate
    :return: The updated TravelersMandatoryCheck object
    """
    return TravelersMandatoryCheckController.update_mandatory_check(check_id=check.check_id, is_fulfilled=check.is_fulfilled)
