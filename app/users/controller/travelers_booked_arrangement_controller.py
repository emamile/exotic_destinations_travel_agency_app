from fastapi import HTTPException, Response

from app.arrangements.exceptions.exceptions import ArrangementNotFoundException
from app.arrangements.services.arrangement_service import ArrangementService
from app.users.exceptions.exceptions import (
    BookedArrangementAlreadyExistsException,
    BookedArrangementNotFoundException,
    TravelerNotFoundException,
)
from app.users.services import TravelerService, TravelersMandatoryCheckService
from app.users.services.travelers_booked_arrangement_service import BookedArrangementService
from app.world_destinations.service import StateInfoService


# This class is used to control the BookedArrangement model.
class BookedArrangementController:
    @staticmethod
    def create_travelers_booked_arrangement(arrangement_id: str, traveler_id: str):
        """
        This function creates a booked arrangement for a traveler

        :param arrangement_id: str, traveler_id: str
        :type arrangement_id: str
        :param traveler_id: The id of the traveler who is booking the arrangement
        :type traveler_id: str
        :return: A list of all the booked arrangements for a traveler.
        """
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            mandatory_infos = StateInfoService.get_all_mandatory_state_infos(state_id=arrangement.state_id)
            if not arrangement.availability:
                raise BookedArrangementNotFoundException(code=400, message="This arrangement is no longer available.")
            booked_arrangement = BookedArrangementService.create_travelers_booked_arrangement(
                arrangement_id=arrangement_id, traveler_id=traveler_id
            )
            for info in mandatory_infos:
                TravelersMandatoryCheckService.create_mandatory_check(booked_arrangement_id=booked_arrangement.id, state_info_id=info.id)
            return booked_arrangement
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except BookedArrangementAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except BookedArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_travelers_booked_arrangements(traveler_id: str):
        """
        It gets the traveler's booked arrangements

        :param traveler_id: str
        :type traveler_id: str
        :return: A list of BookedArrangement objects
        """
        try:
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            booked_arrangements = BookedArrangementService.get_travelers_booked_arrangements(traveler_id=traveler_id)
            return booked_arrangements
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except BookedArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_travelers_booked_arrangement(arrangement_id: str, traveler_id: str):
        """
        This function deletes a booked arrangement by arrangement_id and traveler_id

        :param arrangement_id: str
        :type arrangement_id: str
        :param traveler_id: The ID of the traveler who booked the arrangement
        :type traveler_id: str
        :return: The response is a string with the message that the arrangement is unbooked.
        """
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            if BookedArrangementService.delete_travelers_booked_arrangement(arrangement_id=arrangement_id, traveler_id=traveler_id):
                return Response(status_code=200, content=f"Arrangement with ID {arrangement_id} is unbooked.")
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except BookedArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
