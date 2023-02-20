from sqlalchemy.exc import IntegrityError

from app.arrangements.exceptions import AccommodationAlreadyExistsException, AccommodationNotFoundException
from app.database.db import SessionLocal
from app.arrangements.repository.accommodation_repository import AccommodationRepository


class AccommodationService:

    @staticmethod
    def create_accommodation(name: str, accommodation_type: str, description: str):
        with SessionLocal() as db:
            try:
                accommodation_repository = AccommodationRepository(db)
                return accommodation_repository.create_accommodation(name=name, accommodation_type=accommodation_type, description=description)
            except IntegrityError:
                raise AccommodationAlreadyExistsException(code=400, message="This accommodation already exists in database.")
            except Exception as e:
                raise e

    @staticmethod
    def get_all_accommodations():
        with SessionLocal() as db:
            try:
                accommodation_repository = AccommodationRepository(db)
                accommodations = accommodation_repository.get_all_accommodations()
                if accommodations:
                    return accommodations
                raise AccommodationNotFoundException(code=400, message="Currently, there are no accommodations in database.")
            except Exception as e:
                raise e

    @staticmethod
    def get_accommodation_by_id(accommodation_id: str):
        with SessionLocal() as db:
            try:
                accommodation_repository = AccommodationRepository(db)
                accommodation = accommodation_repository.get_accommodation_by_id(accommodation_id=accommodation_id)
                if accommodation:
                    return accommodation
                raise AccommodationNotFoundException(code=400, message=f"Accommodation with provided ID {accommodation_id} does not exist.")
            except Exception as e:
                raise e

    @staticmethod
    def get_accommodations_by_type(type: str):
        with SessionLocal() as db:
            try:
                accommodation_repository = AccommodationRepository(db)
                accommodations = accommodation_repository.get_accommodations_by_type(type=type)
                if accommodations:
                    return accommodations
                raise AccommodationNotFoundException(code=400, message=f"Currently, there are no accommodations with acronym {type}.")
            except Exception as e:
                raise e

    @staticmethod
    def get_all_types_of_accommodations():
        with SessionLocal() as db:
            try:
                accommodation_repository = AccommodationRepository(db)
                if not accommodation_repository.get_all_types_of_accommodations():
                    raise AccommodationNotFoundException(code=400, message=f"Currently, there are no accommodations in database.")
                return accommodation_repository.get_all_types_of_accommodations()
            except Exception as e:
                raise e

    @staticmethod
    def update_accommodation_description(accommodation_id: str, description: str):
        with SessionLocal() as db:
            try:
                accommodation_repository = AccommodationRepository(db)
                return accommodation_repository.update_accommodation_description(accommodation_id=accommodation_id, description=description)
            except Exception as e:
                raise e

    @staticmethod
    def delete_accommodation_by_id(accommodation_id: str):
        with SessionLocal() as db:
            try:
                accommodation_repository = AccommodationRepository(db)
                if accommodation_repository.delete_accommodation_by_id(accommodation_id=accommodation_id):
                    return True
                raise AccommodationNotFoundException(code=400, message=f"Accommodation with provided ID {accommodation_id} does not exist.")
            except Exception as e:
                raise e



