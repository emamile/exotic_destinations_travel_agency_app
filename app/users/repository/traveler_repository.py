from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.models.traveler import Traveler


class TravelerRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_traveler(self, name: str, surname: str, telephone_number: str, passport_number: str, user_id: str):
        try:
            traveler = Traveler(name=name, surname=surname, telephone_number=telephone_number, passport_number=passport_number, user_id=user_id)
            self.db.add(traveler)
            self.db.commit()
            self.db.refresh(traveler)
            return traveler
        except IntegrityError as e:
            raise e

    def get_all_travelers(self):
        try:
            travelers = self.db.query(Traveler).all()
            return travelers
        except Exception as e:
            raise e

    def get_traveler_by_id(self, traveler_id: str):
        try:
            traveler = self.db.query(Traveler).filter(Traveler.id == traveler_id).first()
            return traveler
        except Exception as e:
            raise e

    def get_traveler_by_passport_number(self, passport_number: str):
        try:
            traveler = self.db.query(Traveler).filter(Traveler.passport_number == passport_number).first()
            return traveler
        except Exception as e:
            raise e

    def update_traveler(self, traveler_id: str, surname: str, telephone_number: str, passport_number: str):
        try:
            traveler = self.db.query(Traveler).filter(Traveler.id == traveler_id).first()
            traveler.surname = surname
            traveler.telephone_number = telephone_number
            traveler.passport_number = passport_number
            self.db.add(traveler)
            self.db.commit()
            self.db.refresh(traveler)
            return traveler
        except Exception as e:
            raise e

    def delete_traveler_by_id(self, traveler_id: str):
        try:
            traveler = self.db.query(Traveler).filter(Traveler.id == traveler_id).first()
            if traveler:
                self.db.delete(traveler)
                self.db.commit()
                return True
            return False
        except Exception as e:
            raise e

