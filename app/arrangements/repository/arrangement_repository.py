from datetime import datetime

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.arrangements.models.arrangement import Arrangement


# > This class is responsible for storing and retrieving arrangements
class ArrangementRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_arrangement(
        self,
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
        It creates an arrangement object and adds it to the database

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
            arrangement = Arrangement(
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
            self.db.add(arrangement)
            self.db.commit()
            self.db.refresh(arrangement)
            return arrangement
        except IntegrityError as e:
            raise e
        except ValueError as e:
            raise e

    def get_all_arrangements_for_state(self, state_id: str):
        """
        It returns all arrangements for a given state

        :param state_id: The id of the state you want to get arrangements for
        :type state_id: str
        :return: A list of all arrangements for a given state.
        """
        try:
            arrangements = self.db.query(Arrangement).filter(Arrangement.state_id == state_id).all()
            return arrangements
        except Exception as e:
            raise e

    def get_all_arrangements(self):
        """
        It returns all the arrangements in the database
        :return: A list of all the arrangements in the database.
        """
        try:
            arrangements = self.db.query(Arrangement).all()
            return arrangements
        except Exception as e:
            raise e

    def get_arrangement_by_id(self, arrangement_id: str):
        """
        It gets an arrangement by id

        :param arrangement_id: The id of the arrangement you want to get
        :type arrangement_id: str
        :return: The arrangement object
        """
        try:
            arrangement = self.db.query(Arrangement).filter(Arrangement.id == arrangement_id).first()
            return arrangement
        except Exception as e:
            raise e

    def get_arrangement_by_code(self, code: str):
        """
        It takes a string as an argument and returns an arrangement object from the database

        :param code: The code of the arrangement to be retrieved
        :type code: str
        :return: The arrangement with the code that is passed in.
        """
        try:
            arrangement = self.db.query(Arrangement).filter(Arrangement.code == code).first()
            return arrangement
        except Exception as e:
            raise e

    def get_arrangements_under_price(self, price: float):
        """
        It returns all arrangements that are under a certain price

        :param price: float
        :type price: float
        :return: A list of Arrangement objects
        """
        try:
            arrangements = self.db.query(Arrangement).filter(Arrangement.price <= price).all()
            return arrangements
        except Exception as e:
            raise e

    def get_arrangements_by_start_date(self, date: str):
        """
        It returns all arrangements that have a date of departure equal to the date passed in as a parameter

        :param date: str
        :type date: str
        :return: A list of arrangements
        """
        try:
            if date == datetime.strptime(date, "%Y-%m-%d"):
                arrangements = self.db.query(Arrangement).filter(Arrangement.date_of_departure == date).all()
                return arrangements
            raise ValueError
        except ValueError as e:
            raise e
        except Exception as e:
            raise e

    def update_arrangements_price_and_availability(self, arrangement_id: str, price: float = None, availability: bool = None):
        """
        It updates the price and availability of an arrangement

        :param arrangement_id: str
        :type arrangement_id: str
        :param price: float = None
        :type price: float
        :param availability: bool = None
        :type availability: bool
        :return: The arrangement object
        """

        try:
            arrangement = self.db.query(Arrangement).filter(Arrangement.id == arrangement_id).first()
            if price is not None:
                arrangement.price = price
            if availability is not None:
                arrangement.availability = availability
            self.db.add(arrangement)
            self.db.commit()
            self.db.refresh(arrangement)
            return arrangement
        except Exception as e:
            raise e

    def delete_arrangement_by_id(self, arrangement_id: str):
        """
        It deletes an arrangement from the database

        :param arrangement_id: The id of the arrangement to be deleted
        :type arrangement_id: str
        :return: A boolean value.
        """
        try:
            arrangement = self.db.query(Arrangement).filter(Arrangement.id == arrangement_id).first()
            if arrangement is None:
                return False
            self.db.delete(arrangement)
            self.db.commit()
            return True
        except Exception as e:
            raise e
