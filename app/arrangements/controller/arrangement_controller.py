from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from app.arrangements.services.arrangement_service import ArrangementService
from app.users.exceptions import TravelerNotFoundException, BookedArrangementNotFoundException
from app.users.services import BookedArrangementService
from app.world_destinations.service import StateService, WorldDestinationService
from app.world_destinations.exceptions.exceptions import StateNotFoundException, WorldDestinationNotFoundException
from app.arrangements.exceptions.exceptions import ArrangementNotFoundException, ArrangementsNotFoundException, \
    DateOfDepartureOrArrivalException


class ArrangementController:

    @staticmethod
    def create_arrangement(name: str, code: str, date_of_departure: str, date_of_arrival: str,
                           duration: int, description: str, air_route_to_the_destination: str,
                           price: float, demandingness: int, availability: bool, included_in_price: str,
                           not_included_in_price: str, state_id: str):
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            arrangement = ArrangementService.create_arrangement(name=name, code=code,
                                                                date_of_departure=date_of_departure,
                                                                date_of_arrival=date_of_arrival,
                                                                duration=duration, description=description,
                                                                air_route_to_the_destination=air_route_to_the_destination,
                                                                price=price, demandingness=demandingness,
                                                                availability=availability,
                                                                included_in_price=included_in_price,
                                                                not_included_in_price=not_included_in_price,
                                                                state_id=state_id
                                                                )
            return arrangement
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except DateOfDepartureOrArrivalException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Arrangement with code {code} already exist.")
        except ValueError:
            raise HTTPException(status_code=400, detail="Bad date format. Date must be in format yyyy-mm-dd.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_arrangements_for_state(state_id: str):
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            arrangements = ArrangementService.get_all_arrangements_for_state(state_id=state_id)
            return arrangements
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_arrangements_for_world_destination(world_destination_id: str):
        try:
            world_destination = WorldDestinationService.get_world_destination_by_id(
                world_destination_id=world_destination_id)
            arrangements = ArrangementService.get_all_arrangements_for_world_destination(
                world_destination_id=world_destination_id)
            return arrangements
        except WorldDestinationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ArrangementsNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_arrangement_by_id(arrangement_id: str):
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            return arrangement
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_arrangement_by_code(code: str):
        try:
            arrangement = ArrangementService.get_arrangement_by_code(code=code)
            return arrangement
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_arrangement_under_price(price: float):
        try:
            arrangements = ArrangementService.get_arrangements_under_price(price=price)
            return arrangements
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_arrangement_by_start_date(date: str):
        try:
            arrangements = ArrangementService.get_arrangements_by_start_date(date=date)
            return arrangements
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_booked_arrangements():
        try:
            booked_arrangements = BookedArrangementService.get_all_booked_arrangements()
            return booked_arrangements
        except BookedArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_booked_arrangement_travelers(arrangement_id: str):
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            travelers = BookedArrangementService.get_all_travelers_for_booked_arrangement(arrangement_id=arrangement_id)
            return travelers
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_arrangements_price_and_availability(arrangement_id: str, price: float, availability: bool):
        try:
            arrangement = ArrangementService.update_arrangements_price_and_availability(arrangement_id=arrangement_id,
                                                                                        price=price,
                                                                                        availability=availability)
            return arrangement
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_arrangement_by_id(arrangement_id: str):
        try:
            if ArrangementService.delete_arrangement_by_id(arrangement_id=arrangement_id):
                return Response(status_code=200, content=f"Arrangement with ID {arrangement_id} is deleted.")
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
