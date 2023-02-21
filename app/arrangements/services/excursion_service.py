from sqlalchemy.exc import IntegrityError

from app.arrangements.exceptions import ExcursionAlreadyExistsException, ExcursionNotFoundException
from app.database.db import SessionLocal
from app.arrangements.repository.excursion_repository import ExcursionRepository


class ExcursionService:

    @staticmethod
    def create_excursion(name: str, price: float, description: str):
        with SessionLocal() as db:
            try:
                excursion_repository = ExcursionRepository(db)
                return excursion_repository.create_excursion(name=name, price=price, description=description)
            except IntegrityError:
                raise ExcursionAlreadyExistsException(code=400, message="This excursion already exists in database.")
            except Exception as e:
                raise e

    @staticmethod
    def get_all_excursions():
        with SessionLocal() as db:
            try:
                excursion_repository = ExcursionRepository(db)
                excursions = excursion_repository.get_all_excursions()
                if excursions:
                    return excursions
                raise ExcursionNotFoundException(code=400, message="Currently, there are no excursions in database.")
            except Exception as e:
                raise e

    @staticmethod
    def get_excursion_by_id(excursion_id: str):
        with SessionLocal() as db:
            try:
                excursion_repository = ExcursionRepository(db)
                excursion = excursion_repository.get_excursion_by_id(excursion_id=excursion_id)
                if excursion:
                    return excursion
                raise ExcursionNotFoundException(code=400, message=f"Excursion with provided ID {excursion_id} does not exist.")
            except Exception as e:
                raise e

    @staticmethod
    def update_excursion_price_and_description(excursion_id: str, price: float, description: str):
        with SessionLocal() as db:
            try:
                excursion_repository = ExcursionRepository(db)
                return excursion_repository.update_excursion_price_and_description(excursion_id=excursion_id, price=price, description=description)
            except Exception as e:
                raise e

    @staticmethod
    def delete_excursion_by_id(excursion_id: str):
        with SessionLocal() as db:
            try:
                excursion_repository = ExcursionRepository(db)
                if excursion_repository.delete_excursion_by_id(excursion_id=excursion_id):
                    return True
                raise ExcursionNotFoundException(code=400, message=f"Excursion with provided ID {excursion_id} does not exist.")
            except Exception as e:
                raise e
