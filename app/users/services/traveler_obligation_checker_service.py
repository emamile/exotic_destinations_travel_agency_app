from sqlalchemy.exc import IntegrityError

from app.database.db import SessionLocal

from app.users.repository.traveler_obligation_checker_repository import TravelerObligationCheckerRepository
from app.users.exceptions.exceptions import TravelerNotFoundException, CheckersNotFoundException


class TravelerObligationCheckerService:

    @staticmethod
    def create_checkers_for_booked_arrangements(is_passport_valid=False, is_visa_valid=False,
                                                is_vaccine_received=False):
        with SessionLocal() as db:
            try:
                traveler_obligation_checker_repository = TravelerObligationCheckerRepository(db)
                return traveler_obligation_checker_repository.create_checkers_for_booked_arrangements(
                    is_passport_valid=is_passport_valid,
                    is_visa_valid=is_visa_valid,
                    is_vaccine_received=is_vaccine_received)
            except IntegrityError as e:
                raise e
            except Exception as e:
                raise e

    @staticmethod
    def get_all_existing_checkers():
        with SessionLocal() as db:
            try:
                traveler_obligation_checker_repository = TravelerObligationCheckerRepository(db)
                checkers = traveler_obligation_checker_repository.get_all_existing_checkers()
                if checkers:
                    return checkers
                raise CheckersNotFoundException(code=400,
                                                message=f"Currently there are no existing checkers.")
            except Exception as e:
                raise e

    @staticmethod
    def get_checkers_for_arrangement(arrangement_id):
        with SessionLocal() as db:
            try:
                traveler_obligation_checker_repository = TravelerObligationCheckerRepository(db)
                checkers = traveler_obligation_checker_repository.get_checkers_for_arrangement(arrangement_id=arrangement_id)
                if checkers:
                    return checkers
                raise CheckersNotFoundException(code=400, message=f"Arrangement with ID {arrangement_id} currently has no checkers.")
            except Exception as e:
                raise e

    @staticmethod
    def get_all_checkers_that_belong_to_traveler(traveler_id: str):
        with SessionLocal() as db:
            try:
                traveler_obligation_checker_repository = TravelerObligationCheckerRepository(db)
                checkers = traveler_obligation_checker_repository.get_all_checkers_that_belong_to_traveler(traveler_id=traveler_id)
                if checkers:
                    return checkers
                raise CheckersNotFoundException(code=400, message=f"Traveler with ID {traveler_id} currently has no checkers.")
            except Exception as e:
                raise e

    @staticmethod
    def get_all_travelers_that_have_all_checkers_valid():
        with SessionLocal() as db:
            try:
                traveler_obligation_checker_repository = TravelerObligationCheckerRepository(db)
                travelers = traveler_obligation_checker_repository.get_all_travelers_that_have_all_checkers_valid()
                if travelers:
                    return travelers
                raise TravelerNotFoundException(code=400, message="There are no travelers that have valid checker.")
            except Exception as e:
                raise e

    @staticmethod
    def get_all_travelers_that_do_not_have_all_checkers_valid():
        with SessionLocal() as db:
            try:
                traveler_obligation_checker_repository = TravelerObligationCheckerRepository(db)
                travelers = traveler_obligation_checker_repository.get_all_travelers_that_do_not_have_all_checkers_valid()
                if travelers:
                    return travelers
                raise TravelerNotFoundException(code=400, message="All travelers have their checkers valid.")
            except Exception as e:
                raise e

    @staticmethod
    def update_travelers_checker_for_arrangement(arrangement_id: str, traveler_id: str, is_passport_valid: bool, is_visa_valid: bool, is_vaccine_received: bool):
        with SessionLocal() as db:
            try:
                traveler_obligation_checker_repository = TravelerObligationCheckerRepository(db)
                checker = traveler_obligation_checker_repository.update_travelers_checker_for_arrangement(arrangement_id=arrangement_id, traveler_id=traveler_id, is_passport_valid=is_passport_valid, is_visa_valid=is_visa_valid, is_vaccine_received=is_vaccine_received)
                return checker
            except Exception as e:
                raise e

    @staticmethod
    def delete_checker_for_traveler_and_arrangement(arrangement_id: str, traveler_id: str):
        with SessionLocal() as db:
            try:
                traveler_obligation_checker_repository = TravelerObligationCheckerRepository(db)
                if traveler_obligation_checker_repository.delete_checker_for_traveler_and_arrangement(arrangement_id=arrangement_id, traveler_id=traveler_id):
                    return True
                raise CheckersNotFoundException(code=400, message=f"Checker for arrangement with ID {arrangement_id} and traveler with ID {traveler_id} does not exist.")
            except Exception as e:
                raise e
