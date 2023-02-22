# Importing the IntegrityError exception from the sqlalchemy.exc module.
from sqlalchemy.exc import IntegrityError

from app.database.db import SessionLocal
from app.users.repository import TravelersMandatoryCheckRepository
from app.world_destinations.exceptions import MandatoryCheckAlreadyExistsException, MandatoryCheckNotFoundException


# This class is used to check if the mandatory fields are filled in the traveler's form
class TravelersMandatoryCheckService:
    @staticmethod
    def create_mandatory_check(booked_arrangement_id: str, state_info_id: str, is_fulfilled: bool = False):
        """
        It creates a mandatory check for a traveler

        :param booked_arrangement_id: str, state_info_id: str, is_fulfilled: bool = False
        :type booked_arrangement_id: str
        :param state_info_id: This is the id of the state that the traveler is in
        :type state_info_id: str
        :param is_fulfilled: bool = False, defaults to False
        :type is_fulfilled: bool (optional)
        :return: The return value is a dictionary with the following keys:
            - id
            - is_fulfilled
            - booked_arrangement_id
            - state_info_id
            - created_at
            - updated_at
        """
        try:
            with SessionLocal() as db:
                mandatory_check_repository = TravelersMandatoryCheckRepository(db)
                return mandatory_check_repository.create_mandatory_check(
                    is_fulfilled=is_fulfilled, booked_arrangement_id=booked_arrangement_id, state_info_id=state_info_id
                )
        except IntegrityError as exc:
            raise MandatoryCheckAlreadyExistsException(code=409, message="This mandatory check already exists.") from exc
        except Exception as e:
            raise e

    @staticmethod
    def get_travelers_mandatory_checks(traveler_id: str):
        """
        It gets the mandatory checks for a traveler with a given ID

        :param traveler_id: str
        :type traveler_id: str
        :return: A list of mandatory checks for a traveler.
        """
        try:
            with SessionLocal() as db:
                mandatory_check_repository = TravelersMandatoryCheckRepository(db)
                checks = mandatory_check_repository.get_travelers_mandatory_checks(traveler_id=traveler_id)
                if checks:
                    return checks
                raise MandatoryCheckNotFoundException(
                    code=400, message=f"Traveler with ID {traveler_id} does not have any mandatory checks for his booked arrangements."
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_all_fulfilled_mandatory_checks():
        """
        It gets all the fulfilled mandatory checks from the database
        :return: A list of all fulfilled mandatory checks.
        """
        try:
            with SessionLocal() as db:
                mandatory_check_repository = TravelersMandatoryCheckRepository(db)
                checks = mandatory_check_repository.get_all_fulfilled_mandatory_checks()
                if checks:
                    return checks
                raise MandatoryCheckNotFoundException(code=400, message="Currently, there are no fulfilled mandatory checks.")
        except Exception as e:
            raise e

    @staticmethod
    def get_all_unfulfilled_mandatory_checks():
        """
        It gets all unfulfilled mandatory checks from the database
        :return: A list of all unfulfilled mandatory checks.
        """
        try:
            with SessionLocal() as db:
                mandatory_check_repository = TravelersMandatoryCheckRepository(db)
                checks = mandatory_check_repository.get_all_unfulfilled_mandatory_checks()
                if checks:
                    return checks
                raise MandatoryCheckNotFoundException(code=400, message="Currently, there are no unfulfilled mandatory checks.")
        except Exception as e:
            raise e

    @staticmethod
    def get_travelers_mandatory_check_by_id(check_id: str):
        """
        It gets a mandatory check by ID

        :param check_id: str
        :type check_id: str
        :return: A list of all the mandatory checks
        """
        try:
            with SessionLocal() as db:
                mandatory_check_repository = TravelersMandatoryCheckRepository(db)
                check = mandatory_check_repository.get_travelers_mandatory_check_by_id(check_id=check_id)
                if check:
                    return check
                raise MandatoryCheckNotFoundException(code=400, message=f"Mandatory check with ID {check_id} does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def update_mandatory_check(check_id: str, is_fulfilled: bool):
        """
        It updates the is_fulfilled field of a mandatory check in the database

        :param check_id: str
        :type check_id: str
        :param is_fulfilled: bool
        :type is_fulfilled: bool
        :return: The updated mandatory check
        """
        try:
            with SessionLocal() as db:
                mandatory_check_repository = TravelersMandatoryCheckRepository(db)
                return mandatory_check_repository.update_mandatory_check(check_id=check_id, is_fulfilled=is_fulfilled)
        except Exception as e:
            raise e

    @staticmethod
    def delete_mandatory_check_by_id(check_id: str):
        """
        It deletes a mandatory check by ID

        :param check_id: str
        :type check_id: str
        :return: A boolean value.
        """
        try:
            with SessionLocal() as db:
                mandatory_check_repository = TravelersMandatoryCheckRepository(db)
                if mandatory_check_repository.delete_mandatory_check_by_id(check_id=check_id):
                    return True
                raise MandatoryCheckNotFoundException(code=400, message=f"Mandatory check with ID {check_id} does not exist.")
        except Exception as e:
            raise e
