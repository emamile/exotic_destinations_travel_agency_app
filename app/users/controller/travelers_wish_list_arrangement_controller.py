from fastapi import HTTPException, Response

from app.arrangements.exceptions.exceptions import ArrangementNotFoundException
from app.arrangements.services.arrangement_service import ArrangementService
from app.users.exceptions.exceptions import (
    TravelerNotFoundException,
    WishListArrangementAlreadyExistsException,
    WishListArrangementNotFoundException,
)
from app.users.services.traveler_service import TravelerService
from app.users.services.travelers_wish_list_arrangement_service import WishListForArrangementsService


# This class is responsible for handling the wish list for arrangements
class WishListForArrangementsController:
    @staticmethod
    def create_travelers_wish_list_arrangement(arrangement_id: str, traveler_id: str):
        """
        It creates a wish list arrangement for a traveler

        :param arrangement_id: str
        :type arrangement_id: str
        :param traveler_id: The ID of the traveler who wants to add the arrangement to their wish list
        :type traveler_id: str
        :return: A wish list arrangement object
        """
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            wish_list_arrangement = WishListForArrangementsService.create_travelers_wish_list_arrangement(
                arrangement_id=arrangement_id, traveler_id=traveler_id
            )
            return wish_list_arrangement
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except WishListArrangementAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_travelers_wish_list_arrangements(traveler_id: str):
        """
        It gets the traveler's wish list arrangements

        :param traveler_id: str
        :type traveler_id: str
        :return: A list of wish list arrangements
        """
        try:
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            wish_list_arrangements = WishListForArrangementsService.get_travelers_wish_list_arrangements(traveler_id=traveler_id)
            return wish_list_arrangements
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except WishListArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_travelers_wish_list_arrangement(arrangement_id: str, traveler_id: str):
        """
        This function deletes an arrangement from a traveler's wish list

        :param arrangement_id: str
        :type arrangement_id: str
        :param traveler_id: str
        :type traveler_id: str
        :return: A list of all the arrangements that are in the traveler's wish list.
        """
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            if WishListForArrangementsService.delete_travelers_wish_list_arrangement(
                arrangement_id=arrangement_id, traveler_id=traveler_id
            ):
                return Response(status_code=200, content=f"Arrangement with ID {arrangement_id} is deleted from your wish list.")
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except WishListArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
