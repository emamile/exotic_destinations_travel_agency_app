# Importing the IntegrityError exception from the sqlalchemy.exc module.
from sqlalchemy.exc import IntegrityError

from app.database.db import SessionLocal
from app.users.exceptions.exceptions import TravelerAlreadyExistsException, TravelerNotFoundException
from app.users.repository.traveler_repository import TravelerRepository


# > This class is responsible for managing the Traveler object
class TravelerService:
    @staticmethod
    def create_traveler(name: str, surname: str, telephone_number: str, passport_number: str, user_id: str):
        """
        It creates a traveler in the database

        :param name: str, surname: str, telephone_number: str, passport_number: str, user_id: str
        :type name: str
        :param surname: str, telephone_number: str, passport_number: str, user_id: str
        :type surname: str
        :param telephone_number: str,
        :type telephone_number: str
        :param passport_number: str
        :type passport_number: str
        :param user_id: str - the id of the user who created the traveler
        :type user_id: str
        :return: The traveler object is being returned.
        """
        try:
            with SessionLocal() as db:
                traveler_repository = TravelerRepository(db)
                return traveler_repository.create_traveler(
                    name=name, surname=surname, telephone_number=telephone_number, passport_number=passport_number, user_id=user_id
                )
        except IntegrityError as exc:
            raise TravelerAlreadyExistsException(
                code=409, message=f"Traveler with passport number {passport_number} already exists."
            ) from exc
        except Exception as e:
            raise e

    @staticmethod
    def get_all_travelers():
        """
        It gets all the travelers from the database
        :return: A list of all travelers
        """
        try:
            with SessionLocal() as db:
                traveler_repository = TravelerRepository(db)
                travelers = traveler_repository.get_all_travelers()
                if travelers:
                    return travelers
                raise TravelerNotFoundException(code=404, message="Currently, there are no existing traveles.")
        except Exception as e:
            raise e

    @staticmethod
    def get_traveler_by_id(traveler_id: str):
        """
        It gets a traveler by ID

        :param traveler_id: str
        :type traveler_id: str
        :return: A traveler object
        """
        try:
            with SessionLocal() as db:
                traveler_repository = TravelerRepository(db)
                traveler = traveler_repository.get_traveler_by_id(traveler_id=traveler_id)
                if traveler:
                    return traveler
                raise TravelerNotFoundException(code=400, message=f"Traveler with provided ID {traveler_id} does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def get_traveler_by_passport_number(passport_number: str):
        """
        It gets a traveler by passport number

        :param passport_number: str
        :type passport_number: str
        :return: A traveler object
        """
        try:
            with SessionLocal() as db:
                traveler_repository = TravelerRepository(db)
                traveler = traveler_repository.get_traveler_by_passport_number(passport_number=passport_number)
                if traveler:
                    return traveler
                raise TravelerNotFoundException(code=400, message=f"Traveler with passport number {passport_number} does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def update_traveler(traveler_id: str, surname: str, telephone_number: str, passport_number: str):
        """
        It updates the traveler's information.

        :param traveler_id: str
        :type traveler_id: str
        :param surname: str
        :type surname: str
        :param telephone_number: str,
        :type telephone_number: str
        :param passport_number: str
        :type passport_number: str
        :return: The updated traveler object.
        """
        try:
            with SessionLocal() as db:
                traveler_repository = TravelerRepository(db)
                return traveler_repository.update_traveler(
                    traveler_id=traveler_id, surname=surname, telephone_number=telephone_number, passport_number=passport_number
                )
        except Exception as e:
            raise e

    @staticmethod
    def delete_traveler_by_id(traveler_id: str):
        """
        It deletes a traveler by ID.

        :param traveler_id: str
        :type traveler_id: str
        :return: A boolean value.
        """
        try:
            with SessionLocal() as db:
                traveler_repository = TravelerRepository(db)
                if traveler_repository.delete_traveler_by_id(traveler_id=traveler_id):
                    return True
                raise TravelerNotFoundException(code=400, message=f"Traveler with provided ID {traveler_id} does not exist.")
        except Exception as e:
            raise e
