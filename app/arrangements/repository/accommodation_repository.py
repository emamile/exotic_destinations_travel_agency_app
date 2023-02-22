from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.arrangements.models.accommodation import Accommodation


# > This class is responsible for retrieving accommodation data from the database
class AccommodationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_accommodation(self, name: str, type: str, description: str):
        """
        It creates an accommodation object and adds it to the database

        :param name: str
        :type name: str
        :param type: str, description: str
        :type type: str
        :param description: str
        :type description: str
        :return: The accommodation object is being returned.
        """
        try:
            accommodation = Accommodation(name=name, type=type, description=description)
            self.db.add(accommodation)
            self.db.commit()
            self.db.refresh(accommodation)
            return accommodation
        except IntegrityError as e:
            raise e

    def get_all_accommodations(self):
        """
        It returns all the accommodations in the database
        :return: A list of all the accommodations in the database.
        """
        try:
            accommodations = self.db.query(Accommodation).all()
            return accommodations
        except Exception as e:
            raise e

    def get_accommodation_by_id(self, accommodation_id: str):
        """
        It gets accommodation by its id

        :param accommodation_id: The id of the accommodation to be retrieved
        :type accommodation_id: str
        :return: The accommodation object
        """
        try:
            accommodation = self.db.query(Accommodation).filter(Accommodation.id == accommodation_id).first()
            return accommodation
        except Exception as e:
            raise e

    def get_accommodations_by_type(self, type: str):
        """
        It returns all accommodations that have a type that contains the string passed in as a parameter

        :param type: str
        :type type: str
        :return: A list of accommodations that match the type.
        """
        try:
            accommodations = self.db.query(Accommodation).filter(Accommodation.type.ilike(f"%{type}%")).all()
            return accommodations
        except Exception as e:
            raise e

    def get_all_types_of_accommodations(self):
        """
        It returns a list of all the types of accommodations in the database
        :return: A list of all the types of accommodations
        """
        try:
            accommodations = self.db.query(Accommodation).all()
            if accommodations:
                types = []
                for accommodation in accommodations:
                    types.append(accommodation.type)
                return types
            return False
        except Exception as e:
            raise e

    def update_accommodation_description(self, accommodation_id: str, description: str):
        """
        It updates the description of an accommodation with the given id

        :param accommodation_id: The id of the accommodation to be updated
        :type accommodation_id: str
        :param description: str
        :type description: str
        :return: accommodation
        """
        try:
            accommodation = self.db.query(Accommodation).filter(Accommodation.id == accommodation_id).first()
            accommodation.description = description
            self.db.add(accommodation)
            self.db.commit()
            self.db.refresh(accommodation)
            return accommodation
        except Exception as e:
            raise e

    def delete_accommodation_by_id(self, accommodation_id: str):
        """
        It deletes accommodation from the database if it exists

        :param accommodation_id: The id of the accommodation to be deleted
        :type accommodation_id: str
        :return: A boolean value.
        """
        try:
            accommodation = self.db.query(Accommodation).filter(Accommodation.id == accommodation_id).first()
            if accommodation:
                self.db.delete(accommodation)
                self.db.commit()
                return True
            return False
        except Exception as e:
            raise e
