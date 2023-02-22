from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.arrangements.models.excursion import Excursion


# > This class is responsible for storing and retrieving excursions from the database
class ExcursionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_excursion(self, name: str, price: float, description: str):
        """
        It creates an excursion object, adds it to the database, commits the changes, and returns the excursion object

        :param name: str
        :type name: str
        :param price: float
        :type price: float
        :param description: str
        :type description: str
        :return: excursion
        """
        try:
            excursion = Excursion(name=name, price=price, description=description)
            self.db.add(excursion)
            self.db.commit()
            self.db.refresh(excursion)
            return excursion
        except IntegrityError as e:
            raise e

    def get_all_excursions(self):
        """
        It returns all the excursions in the database
        :return: A list of all excursions in the database.
        """
        try:
            excursions = self.db.query(Excursion).all()
            return excursions
        except Exception as e:
            raise e

    def get_excursion_by_id(self, excursion_id: str):
        """
        It gets an excursion by its id

        :param excursion_id: The id of the excursion you want to get
        :type excursion_id: str
        :return: The excursion with the given id.
        """
        try:
            excursion = self.db.query(Excursion).filter(Excursion.id == excursion_id).first()
            return excursion
        except Exception as e:
            raise e

    def get_excursions_under_price(self, price: float):
        """
        It returns all excursions that are under a certain price

        :param price: float
        :type price: float
        :return: A list of excursions that are under a certain price.
        """
        try:
            excursions = self.db.query(Excursion).filter(Excursion.price < price).all()
            return excursions
        except Exception as e:
            raise e

    def update_excursion_price_and_description(self, excursion_id: str, price: float = None, description: str = None):
        """
        It updates the price and description of an excursion

        :param excursion_id: str
        :type excursion_id: str
        :param price: float = None
        :type price: float
        :param description: str = None
        :type description: str
        :return: The excursion object
        """
        try:
            excursion = self.db.query(Excursion).filter(Excursion.id == excursion_id).first()
            if price is not None:
                excursion.price = price
            if description is not None:
                excursion.description = description
            self.db.add(excursion)
            self.db.commit()
            self.db.refresh(excursion)
            return excursion
        except Exception as e:
            raise e

    def delete_excursion_by_id(self, excursion_id: str):
        """
        It deletes an excursion from the database if it exists

        :param excursion_id: The id of the excursion to be deleted
        :type excursion_id: str
        :return: True or False
        """
        try:
            excursion = self.db.query(Excursion).filter(Excursion.id == excursion_id).first()
            if excursion:
                self.db.delete(excursion)
                self.db.commit()
                return True
            return False
        except Exception as e:
            raise e
