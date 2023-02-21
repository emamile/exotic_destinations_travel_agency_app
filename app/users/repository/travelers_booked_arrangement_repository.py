from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.models.travelers_booked_arrangement import BookedArrangement
from app.users.models.traveler import Traveler


class BookedArrangementRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_travelers_booked_arrangement(self, arrangement_id: str, traveler_id: str):
        try:
            booked_arrangement = BookedArrangement(arrangement_id=arrangement_id, traveler_id=traveler_id)
            self.db.add(booked_arrangement)
            self.db.commit()
            self.db.refresh(booked_arrangement)
            return booked_arrangement
        except IntegrityError as e:
            raise e

    def get_travelers_booked_arrangements(self, traveler_id: str):
        try:
            booked_arrangements = self.db.query(BookedArrangement).filter(BookedArrangement.traveler_id == traveler_id).all()
            return booked_arrangements
        except Exception as e:
            raise e

    def get_all_travelers_for_booked_arrangement(self, arrangement_id: str):
        try:
            booked_arrangements = self.db.query(BookedArrangement).filter(BookedArrangement.arrangement_id == arrangement_id).all()
            if booked_arrangements:
                travelers = []
                for arrangement in booked_arrangements:
                    travelers.append(self.db.query(Traveler).filter(Traveler.id == arrangement.traveler_id).first())
                return travelers
        except Exception as e:
            raise e

    def get_all_booked_arrangements(self):
        try:
            booked_arrangements = self.db.query(BookedArrangement).all()
            return booked_arrangements
        except Exception as e:
            raise e

    def delete_travelers_booked_arrangement(self, arrangement_id: str, traveler_id: str):
        try:
            booked_arrangement = self.db.query(BookedArrangement).filter(BookedArrangement.arrangement_id == arrangement_id and BookedArrangement.traveler_id == traveler_id).first()
            if booked_arrangement:
                self.db.delete(booked_arrangement)
                self.db.commit()
                return True
            return False
        except Exception as e:
            raise e
