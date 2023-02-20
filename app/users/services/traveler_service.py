from sqlalchemy.exc import IntegrityError

from app.database.db import SessionLocal
from app.users.repository.traveler_repository import TravelerRepository
from app.users.exceptions.exceptions import TravelerNotFoundException, TravelerAlreadyExistsException


class TravelerService:

    @staticmethod
    def create_traveler(name: str, surname: str, telephone_number: str, passport_number: str, user_id: str):
        try:
            with SessionLocal() as db:
                traveler_repository = TravelerRepository(db)
                return traveler_repository.create_traveler(name=name, surname=surname,
                                                           telephone_number=telephone_number,
                                                           passport_number=passport_number, user_id=user_id)
        except IntegrityError:
            raise TravelerAlreadyExistsException(code=400,
                                                 message=f"Traveler with passport number {passport_number} already exists.")
        except Exception as e:
            raise e

    @staticmethod
    def get_all_travelers():
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
        try:
            with SessionLocal() as db:
                traveler_repository = TravelerRepository(db)
                traveler = traveler_repository.get_traveler_by_id(traveler_id=traveler_id)
                if traveler:
                    return traveler
                raise TravelerNotFoundException(code=400,
                                                message=f"Traveler with provided ID {traveler_id} does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def get_traveler_by_passport_number(passport_number: str):
        try:
            with SessionLocal() as db:
                traveler_repository = TravelerRepository(db)
                traveler = traveler_repository.get_traveler_by_passport_number(passport_number=passport_number)
                if traveler:
                    return traveler
                raise TravelerNotFoundException(code=400,
                                                message=f"Traveler with passport number {passport_number} does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def update_traveler(traveler_id: str, surname: str, telephone_number: str, passport_number: str):
        try:
            with SessionLocal() as db:
                traveler_repository = TravelerRepository(db)
                return traveler_repository.update_traveler(traveler_id=traveler_id, surname=surname,
                                                           telephone_number=telephone_number,
                                                           passport_number=passport_number)
        except Exception as e:
            raise e

    @staticmethod
    def delete_traveler_by_id(traveler_id: str):
        try:
            with SessionLocal() as db:
                traveler_repository = TravelerRepository(db)
                if traveler_repository.delete_traveler_by_id(traveler_id=traveler_id):
                    return True
                raise TravelerNotFoundException(code=400,
                                                message=f"Traveler with provided ID {traveler_id} does not exist.")
        except Exception as e:
            raise e
