# Importing the IntegrityError exception from the sqlalchemy.exc module.
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.models.travelers_wish_list_arrangement import WishListForArrangements


# This class is responsible for retrieving and storing wish lists for arrangements
class WishListForArrangementsRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_travelers_wish_list_arrangement(self, arrangement_id: str, traveler_id: str):
        """
        It creates a new wish list arrangement for a traveler

        :param arrangement_id: The arrangement id that the traveler wants to add to their wish list
        :type arrangement_id: str
        :param traveler_id: The id of the traveler who is adding the arrangement to their wish list
        :type traveler_id: str
        :return: The wish list arrangement is being returned.
        """
        try:
            wish_list_arrangement = WishListForArrangements(arrangement_id=arrangement_id, traveler_id=traveler_id)
            self.db.add(wish_list_arrangement)
            self.db.commit()
            self.db.refresh(wish_list_arrangement)
            return wish_list_arrangement
        except IntegrityError as e:
            raise e

    def get_travelers_wish_list_arrangements(self, traveler_id: str):
        """
        It returns a list of all the arrangements that a traveler has added to their wish list

        :param traveler_id: The id of the traveler whose wish list you want to get
        :type traveler_id: str
        :return: A list of all the wish list arrangements for a specific traveler.
        """
        try:
            wish_list_arrangements = self.db.query(WishListForArrangements).filter(WishListForArrangements.traveler_id == traveler_id).all()
            return wish_list_arrangements
        except Exception as e:
            raise e

    def delete_travelers_wish_list_arrangement(self, arrangement_id: str, traveler_id: str):
        """
        It deletes a wish list arrangement from the database

        :param arrangement_id: The arrangement id of the arrangement you want to delete from the traveler's wish list
        :type arrangement_id: str
        :param traveler_id: The id of the traveler who is adding the arrangement to their wish list
        :type traveler_id: str
        :return: A boolean value.
        """
        try:
            wish_list_arrangement = (
                self.db.query(WishListForArrangements)
                .filter(WishListForArrangements.arrangement_id == arrangement_id, WishListForArrangements.traveler_id == traveler_id)
                .first()
            )
            if wish_list_arrangement:
                self.db.delete(wish_list_arrangement)
                self.db.commit()
                return True
            return False
        except Exception as e:
            raise e
