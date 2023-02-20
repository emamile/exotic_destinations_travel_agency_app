from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.arrangements.models.excursion import Excursion


class ExcursionRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_excursion(self, name: str, price: float, description: str):
        try:
            excursion = Excursion(name=name, price=price, description=description)
            self.db.add(excursion)
            self.db.commit()
            self.db.refresh(excursion)
            return excursion
        except IntegrityError as e:
            raise e

    def get_all_excursions(self):
        try:
            excursions = self.db.query(Excursion).all()
            return excursions
        except Exception as e:
            raise e

    def get_excursion_by_id(self, excursion_id: str):
        try:
            excursion = self.db.query(Excursion).filter(Excursion.id == excursion_id).first()
            return excursion
        except Exception as e:
            raise e

    def get_excursions_under_price(self, price: float):
        try:
            excursions = self.db.query(Excursion).filter(Excursion.price < price).all()
            return excursions
        except Exception as e:
            raise e

    def update_excursion_price_and_description(self, excursion_id: str, price: float, description: str):
        try:
            excursion = self.db.query(Excursion).filter(Excursion.id == excursion_id).first()
            excursion.price = price
            excursion.description = description
            self.db.add(excursion)
            self.db.commit()
            self.db.refresh(excursion)
            return excursion
        except Exception as e:
            raise e

    def delete_excursion_by_id(self, excursion_id: str):
        try:
            excursion = self.db.query(Excursion).filter(Excursion.id == excursion_id).first()
            if excursion:
                self.db.delete(excursion)
                self.db.commit()
                return True
            return False
        except Exception as e:
            raise e
