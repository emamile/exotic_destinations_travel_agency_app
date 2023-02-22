# Importing the IntegrityError exception from the sqlalchemy.exc module.
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.models.traveler import Traveler


# This class is a repository for Traveler objects.
class TravelerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_traveler(self, name: str, surname: str, telephone_number: str, passport_number: str, user_id: str):
        """
        It creates a traveler object and adds it to the database

        :param name: str, surname: str, telephone_number: str, passport_number: str, user_id: str
        :type name: str
        :param surname: str, telephone_number: str, passport_number: str, user_id: str
        :type surname: str
        :param telephone_number: str, passport_number: str, user_id: str
        :type telephone_number: str
        :param passport_number: str, user_id: str
        :type passport_number: str
        :param user_id: str
        :type user_id: str
        :return: The traveler object is being returned.
        """

        try:
            traveler = Traveler(
                name=name, surname=surname, telephone_number=telephone_number, passport_number=passport_number, user_id=user_id
            )
            self.db.add(traveler)
            self.db.commit()
            self.db.refresh(traveler)
            return traveler
        except IntegrityError as e:
            raise e

    def get_all_travelers(self):
        """
        It returns all the travelers in the database
        :return: A list of all the travelers in the database.
        """
        try:
            travelers = self.db.query(Traveler).all()
            return travelers
        except Exception as e:
            raise e

    def get_traveler_by_id(self, traveler_id: str):
        """
        It gets a traveler by id

        :param traveler_id: The id of the traveler to be retrieved
        :type traveler_id: str
        :return: A traveler object
        """
        try:
            traveler = self.db.query(Traveler).filter(Traveler.id == traveler_id).first()
            return traveler
        except Exception as e:
            raise e

    def get_traveler_by_passport_number(self, passport_number: str):
        """
        It takes a passport number as a string, and returns a traveler object

        :param passport_number: The passport number of the traveler
        :type passport_number: str
        :return: A traveler object
        """
        try:
            traveler = self.db.query(Traveler).filter(Traveler.passport_number == passport_number).first()
            return traveler
        except Exception as e:
            raise e

    def update_traveler(self, traveler_id: str, surname: str = None, telephone_number: str = None, passport_number: str = None):
        """
        It updates a traveler's details in the database

        :param traveler_id: str - the id of the traveler to be updated
        :type traveler_id: str
        :param surname: str = None, telephone_number: str = None, passport_number: str = None
        :type surname: str
        :param telephone_number: str = None
        :type telephone_number: str
        :param passport_number: str = None
        :type passport_number: str
        :return: The traveler object is being returned.
        """
        try:
            traveler = self.db.query(Traveler).filter(Traveler.id == traveler_id).first()
            if surname is not None:
                traveler.surname = surname
            if telephone_number is not None:
                traveler.telephone_number = telephone_number
            if passport_number is not None:
                traveler.passport_number = passport_number
            self.db.add(traveler)
            self.db.commit()
            self.db.refresh(traveler)
            return traveler
        except Exception as e:
            raise e

    def delete_traveler_by_id(self, traveler_id: str):
        """
        It deletes a traveler from the database if the traveler exists

        :param traveler_id: str
        :type traveler_id: str
        :return: True or False
        """
        try:
            traveler = self.db.query(Traveler).filter(Traveler.id == traveler_id).first()
            if traveler:
                self.db.delete(traveler)
                self.db.commit()
                return True
            return False
        except Exception as e:
            raise e
