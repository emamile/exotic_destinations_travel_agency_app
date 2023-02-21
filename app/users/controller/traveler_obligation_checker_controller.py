from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.users.services.traveler_obligation_checker_service import TravelerObligationCheckerService
from app.users.exceptions.exceptions import CheckersNotFoundException, TravelerNotFoundException
from app.arrangements.services.arrangement_service import ArrangementService
from app.users.services.traveler_service import TravelerService
from app.arrangements.exceptions.exceptions import ArrangementNotFoundException


class TravelerObligationCheckerController:

    @staticmethod
    def create_checkers_for_booked_arrangements(is_passport_valid=False, is_visa_valid=False,
                                                is_vaccine_received=False):
        try:
            checkers = TravelerObligationCheckerService.create_checkers_for_booked_arrangements(
                is_passport_valid=is_passport_valid,
                is_visa_valid=is_visa_valid,
                is_vaccine_received=is_vaccine_received)
            return checkers
        except IntegrityError as e:
            raise HTTPException(status_code=500, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_existing_checkers():
        try:
            checkers = TravelerObligationCheckerService.get_all_existing_checkers()
            return checkers
        except CheckersNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_checkers_for_arrangement(arrangement_id: str):
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            checkers = TravelerObligationCheckerService.get_checkers_for_arrangement(arrangement_id=arrangement_id)
            return checkers
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except CheckersNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_checkers_that_belong_to_traveler(traveler_id: str):
        try:
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            checkers = TravelerObligationCheckerService.get_all_checkers_that_belong_to_traveler(traveler_id=traveler_id)
            return checkers
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except CheckersNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_travelers_that_have_all_checkers_valid():
        try:
            travelers = TravelerObligationCheckerService.get_all_travelers_that_have_all_checkers_valid()
            return travelers
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_travelers_that_do_not_have_all_checkers_valid():
        try:
            travelers = TravelerObligationCheckerService.get_all_travelers_that_do_not_have_all_checkers_valid()
            return travelers
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_travelers_checker_for_arrangement(arrangement_id: str, traveler_id: str, is_passport_valid: bool, is_visa_valid: bool, is_vaccine_received: bool):
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            checker = TravelerObligationCheckerService.update_travelers_checker_for_arrangement(arrangement_id=arrangement_id, traveler_id=traveler_id, is_passport_valid=is_passport_valid, is_visa_valid=is_visa_valid, is_vaccine_received=is_vaccine_received)
            return checker
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except CheckersNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_checker_for_traveler_and_arrangement(arrangement_id: str, traveler_id: str):
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            if TravelerObligationCheckerController.delete_checker_for_traveler_and_arrangement(arrangement_id=arrangement_id, traveler_id=traveler_id):
                return Response(status_code=200, content=f"Checker for traveler with ID {traveler_id} and his booked arrangement with ID {arrangement_id} is deleted.")
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except CheckersNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
