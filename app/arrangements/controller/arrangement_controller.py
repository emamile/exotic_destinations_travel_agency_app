from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.arrangements.exceptions.exceptions import (
    AccommodationNotFoundException,
    ArrangementNotFoundException,
    ArrangementsNotFoundException,
    DateOfDepartureOrArrivalException,
    ExcursionNotFoundException,
    PlanAndProgramNotFoundException,
)
from app.arrangements.services import PlanAndProgramPerDayService
from app.arrangements.services.arrangement_service import ArrangementService
from app.users.exceptions import BookedArrangementNotFoundException, TravelerNotFoundException
from app.users.services import BookedArrangementService
from app.world_destinations.exceptions.exceptions import StateNotFoundException, WorldDestinationNotFoundException
from app.world_destinations.service import StateService, WorldDestinationService


# > This class is responsible for the arrangement of the game
class ArrangementController:
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
        It creates an arrangement

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
            state = StateService.get_state_by_id(state_id=state_id)
            arrangement = ArrangementService.create_arrangement(
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
            return arrangement
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except DateOfDepartureOrArrivalException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except IntegrityError as exc:
            raise HTTPException(status_code=400, detail=f"Arrangement with code {code} already exist.") from exc
        except ValueError as e:
            raise HTTPException(status_code=400, detail="Bad date format. Date must be in format yyyy-mm-dd.") from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_arrangements_for_state(state_id: str):
        """
        > Given a state ID, return all the arrangements for that state

        :param state_id: The state id of the state you want to get arrangements for
        :type state_id: str
        """
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            arrangements = ArrangementService.get_all_arrangements_for_state(state_id=state_id)
            return arrangements
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_arrangements_for_world_destination(world_destination_id: str):
        """
        > Get all arrangements for a given world destination

        :param world_destination_id: The ID of the world destination you want to get arrangements for
        :type world_destination_id: str
        """
        try:
            world_destination = WorldDestinationService.get_world_destination_by_id(world_destination_id=world_destination_id)
            arrangements = ArrangementService.get_all_arrangements_for_world_destination(world_destination_id=world_destination_id)
            return arrangements
        except WorldDestinationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except ArrangementsNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_arrangement_by_id(arrangement_id: str):
        """
        `get_arrangement_by_id` returns an arrangement object given an arrangement ID

        :param arrangement_id: The arrangement ID of the arrangement you want to get
        :type arrangement_id: str
        """
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            return arrangement
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_arrangement_by_code(code: str):
        """
        It takes a string and returns a string

        :param code: The code of the arrangement you want to get
        :type code: str
        """
        try:
            arrangement = ArrangementService.get_arrangement_by_code(code=code)
            return arrangement
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_arrangement_under_price(price: float):
        """
        > This function returns the arrangement that is under the price

        :param price: The price of the arrangement
        :type price: float
        """
        try:
            arrangements = ArrangementService.get_arrangements_under_price(price=price)
            return arrangements
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_arrangement_by_start_date(date: str):
        """
        > This function returns the arrangement that starts on the given date

        :param date: The date of the arrangement you want to get
        :type date: str
        """
        try:
            arrangements = ArrangementService.get_arrangements_by_start_date(date=date)
            return arrangements
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_booked_arrangements():
        """
        It returns all the booked arrangements.
        """
        try:
            booked_arrangements = BookedArrangementService.get_all_booked_arrangements()
            return booked_arrangements
        except BookedArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_booked_arrangement_travelers(arrangement_id: str):
        """
        Get all travelers for a given arrangement

        :param arrangement_id: The arrangement ID of the arrangement you want to get the travelers for
        :type arrangement_id: str
        """
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            travelers = BookedArrangementService.get_all_travelers_for_booked_arrangement(arrangement_id=arrangement_id)
            return travelers
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_arrangements_excursions(arrangement_id: str):
        """
        > This function returns a list of excursions for a given arrangement

        :param arrangement_id: The arrangement ID of the arrangement you want to get the excursions for
        :type arrangement_id: str
        """
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            excursions = PlanAndProgramPerDayService.get_all_excursions_for_arrangement(arrangement_id=arrangement_id)
            return excursions
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except PlanAndProgramNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except ExcursionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_arrangements_accommodations(arrangement_id: str):
        """
        Get all accommodations for a given arrangement

        :param arrangement_id: The ID of the arrangement you want to get accommodations for
        :type arrangement_id: str
        """
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            accommodations = PlanAndProgramPerDayService.get_all_accommodations_for_arrangement(arrangement_id=arrangement_id)
            return accommodations
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except PlanAndProgramNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except AccommodationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_arrangements_excursions_under_price(arrangement_id: str, price: float):
        """
        > This function returns a list of excursions that are under a certain price for a given arrangement

        :param arrangement_id: The id of the arrangement you want to get excursions for
        :type arrangement_id: str
        :param price: The maximum price you want to pay for the excursion
        :type price: float
        """
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            excursions = PlanAndProgramPerDayService.get_all_excursions_for_arrangement_under_price(
                arrangement_id=arrangement_id, price=price
            )
            return excursions
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except PlanAndProgramNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except ExcursionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def update_arrangements_price_and_availability(arrangement_id: str, price: float, availability: bool):
        """
        "Update the price and availability of an arrangement."

        The first line of the function is a docstring. It's a string that describes what the function does. It's a good idea
        to include a docstring for every function you write

        :param arrangement_id: The ID of the arrangement you want to update
        :type arrangement_id: str
        :param price: The price of the arrangement
        :type price: float
        :param availability: True or False
        :type availability: bool
        """
        try:
            arrangement = ArrangementService.update_arrangements_price_and_availability(
                arrangement_id=arrangement_id, price=price, availability=availability
            )
            return arrangement
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_arrangement_by_id(arrangement_id: str):
        """
        Delete an arrangement by its ID

        :param arrangement_id: The ID of the arrangement you want to delete
        :type arrangement_id: str
        """
        try:
            if ArrangementService.delete_arrangement_by_id(arrangement_id=arrangement_id):
                return Response(status_code=200, content=f"Arrangement with ID {arrangement_id} is deleted.")
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
