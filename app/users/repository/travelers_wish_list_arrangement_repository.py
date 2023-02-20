from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.models.travelers_wish_list_arrangement import WishListForArrangements


class WishListForArrangementsRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_travelers_wish_list_arrangement(self, arrangement_id: str, traveler_id: str):
        try:
            wish_list_arrangement = WishListForArrangements(arrangement_id=arrangement_id, traveler_id=traveler_id)
            self.db.add(wish_list_arrangement)
            self.db.commit()
            self.db.refresh(wish_list_arrangement)
            return wish_list_arrangement
        except IntegrityError as e:
            raise e

    def get_travelers_wish_list_arrangements(self, traveler_id: str):
        try:
            wish_list_arrangements = self.db.query(WishListForArrangements).filter(
                WishListForArrangements.traveler_id == traveler_id).all()
            return wish_list_arrangements
        except Exception as e:
            raise e

    def delete_travelers_wish_list_arrangement(self, arrangement_id: str, traveler_id: str):
        try:
            wish_list_arrangement = self.db.query(WishListForArrangements).filter(
                WishListForArrangements.arrangement_id == arrangement_id,
                WishListForArrangements.traveler_id == traveler_id).first()
            if wish_list_arrangement:
                self.db.delete(wish_list_arrangement)
                self.db.commit()
                return True
            return False
        except Exception as e:
            raise e
