from fastapi import HTTPException, Response
from app.users.services.travelers_booked_arrangement_service import BookedArrangementService
from app.users.exceptions.exceptions import BookedArrangementAlreadyExistsException, BookedArrangementNotFoundException, \
    TravelerNotFoundException
from app.arrangements.services.arrangement_service import ArrangementService
from app.users.services.traveler_service import TravelerService
from app.arrangements.exceptions.exceptions import ArrangementNotFoundException


class BookedArrangementController:

    @staticmethod
    def create_travelers_booked_arrangement(arrangement_id: str, traveler_id: str):
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            booked_arrangement = BookedArrangementService.create_travelers_booked_arrangement(
                arrangement_id=arrangement_id, traveler_id=traveler_id)
            return booked_arrangement
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except BookedArrangementAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_travelers_booked_arrangements(traveler_id: str):
        try:
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            booked_arrangements = BookedArrangementService.get_travelers_booked_arrangements(traveler_id=traveler_id)
            return booked_arrangements
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except BookedArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_travelers_booked_arrangement(arrangement_id: str, traveler_id: str):
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            if BookedArrangementService.delete_travelers_booked_arrangement(arrangement_id=arrangement_id,
                                                                            traveler_id=traveler_id):
                return Response(status_code=200, content=f"Arrangement with ID {arrangement_id} is unbooked.")
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except BookedArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
