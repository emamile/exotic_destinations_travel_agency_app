# Importing the IntegrityError exception from the sqlalchemy.exc module.
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.models.traveler import Traveler
from app.users.models.travelers_booked_arrangement import BookedArrangement


# This class is responsible for retrieving and storing booked arrangements
class BookedArrangementRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_travelers_booked_arrangement(self, arrangement_id: str, traveler_id: str):
        """
        It creates a new BookedArrangement object and adds it to the database

        :param arrangement_id: str
        :type arrangement_id: str
        :param traveler_id: The id of the traveler who booked the arrangement
        :type traveler_id: str
        :return: the booked_arrangement object.
        """
        try:
            booked_arrangement = BookedArrangement(arrangement_id=arrangement_id, traveler_id=traveler_id)
            self.db.add(booked_arrangement)
            self.db.commit()
            self.db.refresh(booked_arrangement)
            return booked_arrangement
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def get_travelers_booked_arrangements(self, traveler_id: str):
        """
        This function returns all the booked arrangements for a given traveler

        :param traveler_id: str
        :type traveler_id: str
        :return: A list of BookedArrangement objects
        """
        try:
            booked_arrangements = self.db.query(BookedArrangement).filter(BookedArrangement.traveler_id == traveler_id).all()
            return booked_arrangements
        except Exception as e:
            raise e

    def get_all_travelers_for_booked_arrangement(self, arrangement_id: str):
        """
        It returns a list of all the travelers who have booked a particular arrangement

        :param arrangement_id: str
        :type arrangement_id: str
        :return: A list of all the travelers that have booked a specific arrangement.
        """
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
        """
        It returns all the booked arrangements from the database
        :return: A list of all the booked arrangements.
        """
        try:
            booked_arrangements = self.db.query(BookedArrangement).all()
            return booked_arrangements
        except Exception as e:
            raise e

    def delete_travelers_booked_arrangement(self, arrangement_id: str, traveler_id: str):
        """
        It deletes a booked arrangement from the database if it exists

        :param arrangement_id: The id of the arrangement that the traveler is booked on
        :type arrangement_id: str
        :param traveler_id: The id of the traveler who booked the arrangement
        :type traveler_id: str
        :return: A list of all the booked arrangements for a traveler
        """
        try:
            booked_arrangement = (
                self.db.query(BookedArrangement)
                .filter(BookedArrangement.arrangement_id == arrangement_id and BookedArrangement.traveler_id == traveler_id)
                .first()
            )
            if booked_arrangement:
                self.db.delete(booked_arrangement)
                self.db.commit()
                return True
            return False
        except Exception as e:
            raise e
