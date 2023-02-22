from sqlalchemy.exc import IntegrityError

from app.arrangements.exceptions import AccommodationAlreadyExistsException, AccommodationNotFoundException
from app.arrangements.repository.accommodation_repository import AccommodationRepository
from app.database.db import SessionLocal


# > This class provides a service for managing accommodations
class AccommodationService:
    @staticmethod
    def create_accommodation(name: str, type: str, description: str):
        """
        It creates accommodation in the database

        :param name: str
        :type name: str
        :param type: str
        :type type: str
        :param description: str
        :type description: str
        :return: The accommodation object is being returned.
        """
        try:
            with SessionLocal() as db:
                accommodation_repository = AccommodationRepository(db)
                return accommodation_repository.create_accommodation(name=name, type=type, description=description)
        except IntegrityError as exc:
            raise AccommodationAlreadyExistsException(code=409, message="This accommodation already exists in database.") from exc
        except Exception as e:
            raise e

    @staticmethod
    def get_all_accommodations():
        """
        It gets all accommodations from the database
        :return: A list of all accommodations in the database.
        """
        try:
            with SessionLocal() as db:
                accommodation_repository = AccommodationRepository(db)
                accommodations = accommodation_repository.get_all_accommodations()
                if accommodations:
                    return accommodations
                raise AccommodationNotFoundException(code=400, message="Currently, there are no accommodations in database.")
        except Exception as e:
            raise e

    @staticmethod
    def get_accommodation_by_id(accommodation_id: str):
        """
        It gets accommodation by its ID

        :param accommodation_id: The ID of the accommodation you want to get
        :type accommodation_id: str
        :return: Accommodation object
        """
        try:
            with SessionLocal() as db:
                accommodation_repository = AccommodationRepository(db)
                accommodation = accommodation_repository.get_accommodation_by_id(accommodation_id=accommodation_id)
                if accommodation:
                    return accommodation
                raise AccommodationNotFoundException(code=400, message=f"Accommodation with provided ID {accommodation_id} does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def get_accommodations_by_type(type: str):
        """
        It gets all accommodations of a given type

        :param type: str
        :type type: str
        :return: A list of accommodations.
        """
        try:
            with SessionLocal() as db:
                accommodation_repository = AccommodationRepository(db)
                accommodations = accommodation_repository.get_accommodations_by_type(type=type)
                if accommodations:
                    return accommodations
                raise AccommodationNotFoundException(code=400, message=f"Currently, there are no accommodations with acronym {type}.")
        except Exception as e:
            raise e

    @staticmethod
    def get_all_types_of_accommodations():
        """
        It gets all types of accommodations from the database
        :return: A list of all types of accommodations.
        """
        try:
            with SessionLocal() as db:
                accommodation_repository = AccommodationRepository(db)
                if not accommodation_repository.get_all_types_of_accommodations():
                    raise AccommodationNotFoundException(code=400, message="Currently, there are no accommodations in database.")
                return accommodation_repository.get_all_types_of_accommodations()
        except Exception as e:
            raise e

    @staticmethod
    def update_accommodation_description(accommodation_id: str, description: str):
        """
        It updates the description of accommodation with the given accommodation_id

        :param accommodation_id: str
        :type accommodation_id: str
        :param description: str
        :type description: str
        :return: The accommodation object
        """
        try:
            with SessionLocal() as db:
                accommodation_repository = AccommodationRepository(db)
                return accommodation_repository.update_accommodation_description(accommodation_id=accommodation_id, description=description)
        except Exception as e:
            raise e

    @staticmethod
    def delete_accommodation_by_id(accommodation_id: str):
        """
        It deletes accommodation by its ID.

        :param accommodation_id: str
        :type accommodation_id: str
        :return: A list of Accommodation objects
        """
        try:
            with SessionLocal() as db:
                accommodation_repository = AccommodationRepository(db)
                if accommodation_repository.delete_accommodation_by_id(accommodation_id=accommodation_id):
                    return True
                raise AccommodationNotFoundException(code=400, message=f"Accommodation with provided ID {accommodation_id} does not exist.")
        except Exception as e:
            raise e
