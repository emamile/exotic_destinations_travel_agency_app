from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.arrangements.models.accommodation import Accommodation


class AccommodationRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_accommodation(self, name: str, type: str, description: str):
        try:
            accommodation = Accommodation(name=name, type=type, description=description)
            self.db.add(accommodation)
            self.db.commit()
            self.db.refresh(accommodation)
            return accommodation
        except IntegrityError as e:
            raise e

    def get_all_accommodations(self):
        try:
            accommodations = self.db.query(Accommodation).all()
            return accommodations
        except Exception as e:
            raise e

    def get_accommodation_by_id(self, accommodation_id: str):
        try:
            accommodation = self.db.query(Accommodation).filter(Accommodation.id == accommodation_id).first()
            return accommodation
        except Exception as e:
            raise e

    def get_accommodations_by_type(self, type: str):
        try:
            accommodations = self.db.query(Accommodation).filter(Accommodation.type.ilike(f"%{type}%")).all()
            return accommodations
        except Exception as e:
            raise e

    def get_all_types_of_accommodations(self):
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
        try:
            accommodation = self.db.query(Accommodation).filter(Accommodation.id == accommodation_id).first()
            if accommodation:
                self.db.delete(accommodation)
                self.db.commit()
                return True
            return False
        except Exception as e:
            raise e
