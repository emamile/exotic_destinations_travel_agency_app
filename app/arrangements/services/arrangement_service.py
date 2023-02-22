from sqlalchemy.exc import IntegrityError

from app.arrangements.exceptions import (
    ArrangementAlreadyExistsException,
    ArrangementNotFoundException,
    ArrangementsNotFoundException,
    DateOfDepartureOrArrivalException,
)
from app.arrangements.repository.arrangement_repository import ArrangementRepository
from app.database.db import SessionLocal
from app.world_destinations.service import StateService, WorldDestinationService


# > This class is responsible for arranging the flowers
class ArrangementService:
    @staticmethod
    def create_arrangement(
        name: str,
        code: str,
        date_of_departure: str,
        date_of_arrival: str,
        duration: int,
        description: str,
        air_route_to_the_destination: str,
        price: float,
        demandingness: int,
        availability: bool,
        included_in_price: str,
        not_included_in_price: str,
        state_id: str,
    ):
        """
        It creates an arrangement in the database

        :param name: str,
        :type name: str
        :param code: str,
        :type code: str
        :param date_of_departure: str,
        :type date_of_departure: str
        :param date_of_arrival: str,
        :type date_of_arrival: str
        :param duration: int,
        :type duration: int
        :param description: str,
        :type description: str
        :param air_route_to_the_destination: str,
        :type air_route_to_the_destination: str
        :param price: float,
        :type price: float
        :param demandingness: int,
        :type demandingness: int
        :param availability: bool,
        :type availability: bool
        :param included_in_price: str,
        :type included_in_price: str
        :param not_included_in_price: str,
        :type not_included_in_price: str
        :param state_id: str,
        :type state_id: str
        :return: Arrangement object
        """

        try:
            with SessionLocal() as db:
                arrangement_repository = ArrangementRepository(db)
                if date_of_departure < date_of_arrival:
                    return arrangement_repository.create_arrangement(
                        name=name,
                        code=code,
                        date_of_departure=date_of_departure,
                        date_of_arrival=date_of_arrival,
                        duration=duration,
                        description=description,
                        air_route_to_the_destination=air_route_to_the_destination,
                        price=price,
                        demandingness=demandingness,
                        availability=availability,
                        included_in_price=included_in_price,
                        not_included_in_price=not_included_in_price,
                        state_id=state_id,
                    )
                raise DateOfDepartureOrArrivalException(code=400, message="Date of departure must be before date of arrival!")
        except IntegrityError as exc:
            raise ArrangementAlreadyExistsException(code=409, message=f"Arrangement with code {code} already exists.") from exc
        except Exception as e:
            raise e

    @staticmethod
    def get_all_arrangements_for_state(state_id: str):
        """
        It gets all arrangements for a given state

        :param state_id: The ID of the state for which you want to get all arrangements
        :type state_id: str
        :return: A list of all arrangements for a given state.
        """
        try:
            with SessionLocal() as db:
                arrangement_repository = ArrangementRepository(db)
                arrangements = arrangement_repository.get_all_arrangements_for_state(state_id=state_id)
                if arrangements:
                    return arrangements
                raise ArrangementNotFoundException(code=400, message=f"Currently there are no arrangements for state with ID {state_id}.")
        except Exception as e:
            raise e

    @staticmethod
    def get_all_arrangements():
        """
        It gets all the arrangements from the database
        :return: A list of all the arrangements in the database.
        """
        try:
            with SessionLocal() as db:
                arrangement_repository = ArrangementRepository(db)
                return arrangement_repository.get_all_arrangements()
        except Exception as e:
            raise e

    @staticmethod
    def get_all_arrangements_for_world_destination(world_destination_id: str):
        """
        It gets all arrangements for a world destination by getting all states for the world destination and then getting
        all arrangements for each state

        :param world_destination_id: str
        :type world_destination_id: str
        :return: A list of all arrangements for a given world destination.
        """
        try:
            world_destination = WorldDestinationService.get_world_destination_by_id(world_destination_id=world_destination_id)
            states = StateService.get_all_states_for_world_destination(world_destination_id=world_destination_id)
            arrangements_lst = []
            for state in states:
                arrangements = ArrangementService.get_all_arrangements_for_state(state_id=state.id)
                if ArrangementNotFoundException:
                    pass
                arrangements_lst.append(arrangements)
            if not arrangements_lst:
                raise ArrangementsNotFoundException(
                    code=400, message=f"World destination with ID {world_destination_id} currently has no arrangements."
                )
            return arrangements_lst
        except Exception as e:
            raise e

    @staticmethod
    def get_arrangement_by_id(arrangement_id: str):
        """
        It gets an arrangement by its ID

        :param arrangement_id: The ID of the arrangement you want to get
        :type arrangement_id: str
        :return: Arrangement object
        """
        try:
            with SessionLocal() as db:
                arrangement_repository = ArrangementRepository(db)
                arrangement = arrangement_repository.get_arrangement_by_id(arrangement_id=arrangement_id)
                if arrangement:
                    return arrangement
                raise ArrangementNotFoundException(code=400, message=f"Arrangement with provided ID {arrangement_id} does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def get_arrangement_by_code(code: str):
        """
        It gets an arrangement by code

        :param code: The code of the arrangement you want to get
        :type code: str
        :return: Arrangement object
        """
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
        """
        It gets all the arrangements under a certain price

        :param price: float
        :type price: float
        :return: A list of Arrangement objects.
        """
        try:
            with SessionLocal() as db:
                arrangement_repository = ArrangementRepository(db)
                arrangements = arrangement_repository.get_arrangements_under_price(price=price)
                if arrangements:
                    return arrangements
                raise ArrangementNotFoundException(code=400, message=f"We currently don't have any arrangements under price {price}.")
        except Exception as e:
            raise e

    @staticmethod
    def get_arrangements_by_start_date(date: str):
        """
        It gets all the arrangements from the database that have a start date equal to the date passed as a parameter

        :param date: str
        :type date: str
        :return: A list of arrangements.
        """
        try:
            with SessionLocal() as db:
                arrangement_repository = ArrangementRepository(db)
                arrangements = arrangement_repository.get_arrangements_by_start_date(date=date)
                if arrangements:
                    return arrangements
                raise ArrangementNotFoundException(code=400, message=f"Currently, there are no arrangements for date {date}.")
        except Exception as e:
            raise e

    @staticmethod
    def update_arrangements_price_and_availability(arrangement_id: str, price: float, availability: bool):
        """
        It updates the price and availability of an arrangement with the provided arrangement ID

        :param arrangement_id: str
        :type arrangement_id: str
        :param price: float
        :type price: float
        :param availability: bool
        :type availability: bool
        :return: The updated arrangement.
        """
        try:
            with SessionLocal() as db:
                arrangement_repository = ArrangementRepository(db)
                arrangement = arrangement_repository.get_arrangement_by_id(arrangement_id=arrangement_id)
                if arrangement:
                    return arrangement_repository.update_arrangements_price_and_availability(
                        arrangement_id=arrangement_id, price=price, availability=availability
                    )
                raise ArrangementNotFoundException(code=400, message=f"Arrangement with provided ID {arrangement_id} does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def delete_arrangement_by_id(arrangement_id: str):
        """
        It deletes an arrangement from the database by its ID

        :param arrangement_id: str
        :type arrangement_id: str
        :return: A list of all arrangements
        """
        try:
            with SessionLocal() as db:
                arrangement_repository = ArrangementRepository(db)
                if arrangement_repository.delete_arrangement_by_id(arrangement_id=arrangement_id):
                    return True
                raise ArrangementNotFoundException(code=400, message=f"Arrangement with provided ID {arrangement_id} does not exist.")
        except Exception as e:
            raise e
