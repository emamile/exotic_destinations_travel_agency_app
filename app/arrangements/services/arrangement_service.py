from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.arrangements.exceptions import ArrangementNotFoundException, DateOfDepartureOrArrivalException, \
    ArrangementAlreadyExistsException, ArrangementsNotFoundException
from app.database.db import SessionLocal
from app.arrangements.repository.arrangement_repository import ArrangementRepository
from app.world_destinations.service import WorldDestinationService, StateService


class ArrangementService:

    @staticmethod
    def create_arrangement(name: str, code: str, date_of_departure: str, date_of_arrival: str,
                           duration: int, description: str, air_route_to_the_destination: str,
                           price: float, demandingness: int, availability: bool, included_in_price: str,
                           not_included_in_price: str, state_id: str):
        try:
            with SessionLocal() as db:
                arrangement_repository = ArrangementRepository(db)
                if date_of_departure < date_of_arrival:
                    return arrangement_repository.create_arrangement(name=name, code=code,
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
                raise DateOfDepartureOrArrivalException(code=400,
                                                        message="Date of departure must be before date of arrival!")
        except IntegrityError:
            raise ArrangementAlreadyExistsException(code=400, message=f"Arrangement with code {code} already exists.")
        except Exception as e:
            raise e

    @staticmethod
    def get_all_arrangements_for_state(state_id: str):
        try:
            with SessionLocal() as db:
                arrangement_repository = ArrangementRepository(db)
                arrangements = arrangement_repository.get_all_arrangements_for_state(state_id=state_id)
                if arrangements:
                    return arrangements
                raise ArrangementNotFoundException(code=400,
                                                   message=f"Currently there are no arrangements for state with ID {state_id}.")
        except Exception as e:
            raise e

    @staticmethod
    def get_all_arrangements_for_world_destination(world_destination_id: str):
        try:
            world_destination = WorldDestinationService.get_world_destination_by_id(
                world_destination_id=world_destination_id)
            states = StateService.get_all_states_for_world_destination(world_destination_id=world_destination_id)
            arrangements_lst = []
            for state in states:
                arrangements = ArrangementService.get_all_arrangements_for_state(state_id=state.id)
                if ArrangementNotFoundException:
                    pass
                arrangements_lst.append(arrangements)
            if not arrangements_lst:
                raise ArrangementsNotFoundException(code=400, message=f"World destination with ID {world_destination_id} currently has no arrangements.")
            return arrangements_lst
        except Exception as e:
            raise e

    @staticmethod
    def get_arrangement_by_id(arrangement_id: str):
        try:
            with SessionLocal() as db:
                arrangement_repository = ArrangementRepository(db)
                arrangement = arrangement_repository.get_arrangement_by_id(arrangement_id=arrangement_id)
                if arrangement:
                    return arrangement
                raise ArrangementNotFoundException(code=400,
                                                   message=f"Arrangement with provided ID {arrangement_id} does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def get_arrangement_by_code(code: str):
        try:
            with SessionLocal() as db:
                arrangement_repository = ArrangementRepository(db)
                arrangement = arrangement_repository.get_arrangement_by_code(code=code)
                if arrangement:
                    return arrangement
                raise ArrangementNotFoundException(code=400, message=f"Arrangement with code {code} does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def get_arrangements_under_price(price: float):
        try:
            with SessionLocal() as db:
                arrangement_repository = ArrangementRepository(db)
                arrangements = arrangement_repository.get_arrangements_under_price(price=price)
                if arrangements:
                    return arrangements
                raise ArrangementNotFoundException(code=400,
                                                   message=f"We currently don't have any arrangements under price {price}.")
        except Exception as e:
            raise e

    @staticmethod
    def get_arrangements_by_start_date(date: str):
        try:
            with SessionLocal() as db:
                arrangement_repository = ArrangementRepository(db)
                arrangements = arrangement_repository.get_arrangements_by_start_date(date=date)
                if arrangements:
                    return arrangements
                raise ArrangementNotFoundException(code=400,
                                                   message=f"Currently, there are no arrangements for date {date}.")
        except Exception as e:
            raise e

    @staticmethod
    def update_arrangements_price_and_availability(arrangement_id: str, price: float, availability: bool):
        try:
            with SessionLocal() as db:
                arrangement_repository = ArrangementRepository(db)
                arrangement = arrangement_repository.get_arrangement_by_id(arrangement_id=arrangement_id)
                if arrangement:
                    return arrangement_repository.update_arrangements_price_and_availability(
                        arrangement_id=arrangement_id, price=price, availability=availability)
                raise ArrangementNotFoundException(code=400,
                                                   message=f"Arrangement with provided ID {arrangement_id} does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def delete_arrangement_by_id(arrangement_id: str):
        try:
            with SessionLocal() as db:
                arrangement_repository = ArrangementRepository(db)
                if arrangement_repository.delete_arrangement_by_id(arrangement_id=arrangement_id):
                    return True
                raise ArrangementNotFoundException(code=400,
                                                   message=f"Arrangement with provided ID {arrangement_id} does not exist.")
        except Exception as e:
            raise e
