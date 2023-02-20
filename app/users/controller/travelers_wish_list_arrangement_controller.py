from fastapi import HTTPException, Response
from app.users.services.travelers_wish_list_arrangement_service import WishListForArrangementsService
from app.users.exceptions.exceptions import WishListArrangementAlreadyExistsException, \
    WishListArrangementNotFoundException, TravelerNotFoundException
from app.arrangements.services.arrangement_service import ArrangementService
from app.users.services.traveler_service import TravelerService
from app.arrangements.exceptions.exceptions import ArrangementNotFoundException


class WishListForArrangementsController:

    @staticmethod
    def create_travelers_wish_list_arrangement(arrangement_id: str, traveler_id: str):
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            wish_list_arrangement = WishListForArrangementsService.create_travelers_wish_list_arrangement(
                arrangement_id=arrangement_id, traveler_id=traveler_id)
            return wish_list_arrangement
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except WishListArrangementAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_travelers_wish_list_arrangements(traveler_id: str):
        try:
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            wish_list_arrangements = WishListForArrangementsService.get_travelers_wish_list_arrangements(
                traveler_id=traveler_id)
            return wish_list_arrangements
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except WishListArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_travelers_wish_list_arrangement(arrangement_id: str, traveler_id: str):
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            if WishListForArrangementsService.delete_travelers_wish_list_arrangement(arrangement_id=arrangement_id,
                                                                                     traveler_id=traveler_id):
                return Response(status_code=200,
                                content=f"Arrangement with ID {arrangement_id} is deleted from your wish list.")
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except WishListArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
