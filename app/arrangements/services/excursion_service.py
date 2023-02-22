from sqlalchemy.exc import IntegrityError

from app.arrangements.exceptions import ExcursionAlreadyExistsException, ExcursionNotFoundException
from app.arrangements.repository.excursion_repository import ExcursionRepository
from app.database.db import SessionLocal


# > This class is responsible for managing the excursions
class ExcursionService:
    @staticmethod
    def create_excursion(name: str, price: float, description: str):
        """
        "Create an excursion in the database."

        The function takes three arguments: name, price, and description. The name and description are strings, and the
        price is a float

        :param name: str
        :type name: str
        :param price: float
        :type price: float
        :param description: str
        :type description: str
        :return: The excursion object
        """
        try:
            with SessionLocal() as db:
                excursion_repository = ExcursionRepository(db)
                return excursion_repository.create_excursion(name=name, price=price, description=description)
        except IntegrityError as exc:
            raise ExcursionAlreadyExistsException(code=409, message="This excursion already exists in database.") from exc
        except Exception as e:
            raise e

    @staticmethod
    def get_all_excursions():
        """
        It gets all excursions from the database
        :return: A list of all excursions in the database.
        """
        try:
            with SessionLocal() as db:
                excursion_repository = ExcursionRepository(db)
                excursions = excursion_repository.get_all_excursions()
                if excursions:
                    return excursions
                raise ExcursionNotFoundException(code=400, message="Currently, there are no excursions in database.")
        except Exception as e:
            raise e

    @staticmethod
    def get_excursion_by_id(excursion_id: str):
        """
        > This function gets an excursion by its ID

        :param excursion_id: The ID of the excursion you want to get
        :type excursion_id: str
        :return: The excursion object
        """
        try:
            with SessionLocal() as db:
                excursion_repository = ExcursionRepository(db)
                excursion = excursion_repository.get_excursion_by_id(excursion_id=excursion_id)
                if excursion:
                    return excursion
                raise ExcursionNotFoundException(code=400, message=f"Excursion with provided ID {excursion_id} does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def update_excursion_price_and_description(excursion_id: str, price: float, description: str):
        """
        It updates the price and description of an excursion

        :param excursion_id: str
        :type excursion_id: str
        :param price: float
        :type price: float
        :param description: str
        :type description: str
        :return: The excursion object
        """
        try:
            with SessionLocal() as db:
                excursion_repository = ExcursionRepository(db)
                return excursion_repository.update_excursion_price_and_description(
                    excursion_id=excursion_id, price=price, description=description
                )
        except Exception as e:
            raise e

    @staticmethod
    def delete_excursion_by_id(excursion_id: str):
        """
        It deletes an excursion from the database by its ID

        :param excursion_id: str
        :type excursion_id: str
        :return: True or False
        """
        try:
            with SessionLocal() as db:
                excursion_repository = ExcursionRepository(db)
                if excursion_repository.delete_excursion_by_id(excursion_id=excursion_id):
                    return True
                raise ExcursionNotFoundException(code=400, message=f"Excursion with provided ID {excursion_id} does not exist.")
        except Exception as e:
            raise e
