from fastapi import HTTPException, Response

from app.users.exceptions.exceptions import BookedArrangementNotFoundException, TravelerNotFoundException
from app.users.services import TravelerService, TravelersMandatoryCheckService
from app.world_destinations.exceptions import MandatoryCheckNotFoundException


# This class is used to check if the mandatory fields are filled in the traveler's form
class TravelersMandatoryCheckController:
    @staticmethod
    def get_travelers_mandatory_checks(traveler_id: str):
        """
        It gets a traveler's mandatory checks

        :param traveler_id: str
        :type traveler_id: str
        :return: A list of mandatory checks for a traveler
        """
        try:
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            return TravelersMandatoryCheckService.get_travelers_mandatory_checks(traveler_id=traveler_id)
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except MandatoryCheckNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except BookedArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_fulfilled_mandatory_checks():
        """
        It returns all fulfilled mandatory checks
        :return: A list of all fulfilled mandatory checks.
        """
        try:
            return TravelersMandatoryCheckService.get_all_fulfilled_mandatory_checks()
        except MandatoryCheckNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except BookedArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_unfulfilled_mandatory_checks():
        """
        It returns all unfulfilled mandatory checks for all travelers
        :return: A list of all unfulfilled mandatory checks.
        """
        try:
            return TravelersMandatoryCheckService.get_all_unfulfilled_mandatory_checks()
        except MandatoryCheckNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except BookedArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_travelers_mandatory_check_by_id(check_id: str):
        """
        `get_travelers_mandatory_check_by_id` returns a `TravelersMandatoryCheck` object given a `check_id` string

        :param check_id: The ID of the check you want to retrieve
        :type check_id: str
        :return: A list of TravelersMandatoryCheck objects
        """
        try:
            return TravelersMandatoryCheckService.get_travelers_mandatory_check_by_id(check_id=check_id)
        except MandatoryCheckNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def update_mandatory_check(check_id: str, is_fulfilled: bool):
        """
        It updates the mandatory check of a traveler.

        :param check_id: The id of the check you want to update
        :type check_id: str
        :param is_fulfilled: boolean
        :type is_fulfilled: bool
        :return: The updated mandatory check
        """
        try:
            check = TravelersMandatoryCheckService.get_travelers_mandatory_check_by_id(check_id=check_id)
            return TravelersMandatoryCheckService.update_mandatory_check(check_id=check_id, is_fulfilled=is_fulfilled)
        except MandatoryCheckNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_mandatory_check_by_id(check_id: str):
        """
        It deletes a mandatory check by ID.

        :param check_id: str
        :type check_id: str
        :return: The response is a string with the message "Mandatory check with ID {check_id} is deleted."
        """
        try:
            if TravelersMandatoryCheckService.delete_mandatory_check_by_id(check_id=check_id):
                return Response(status_code=200, content=f"Mandatory check with ID {check_id} is deleted.")
        except MandatoryCheckNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
