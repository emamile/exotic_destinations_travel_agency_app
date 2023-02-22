# Importing the IntegrityError exception from the sqlalchemy.exc module.
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import BookedArrangementNotFoundException
from app.users.models import BookedArrangement, TravelersMandatoryCheck


# This class is responsible for retrieving the mandatory check information for a given traveler
class TravelersMandatoryCheckRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_mandatory_check(self, booked_arrangement_id: str, state_info_id: str, is_fulfilled: bool = False):
        """
        It creates a new row in the database table "TravelersMandatoryCheck" with the given parameters

        :param booked_arrangement_id: The id of the booked arrangement
        :type booked_arrangement_id: str
        :param state_info_id: This is the id of the state_info object that is created when a user enters a state
        :type state_info_id: str
        :param is_fulfilled: bool = False, defaults to False
        :type is_fulfilled: bool (optional)
        :return: A new instance of TravelersMandatoryCheck
        """
        try:
            check = TravelersMandatoryCheck(
                is_fulfilled=is_fulfilled, booked_arrangement_id=booked_arrangement_id, state_info_id=state_info_id
            )
            self.db.add(check)
            self.db.commit()
            self.db.refresh(check)
            return check
        except IntegrityError as e:
            raise e

    def get_travelers_mandatory_checks(self, traveler_id: str):
        """
        It returns a list of lists of TravelersMandatoryCheck objects

        :param traveler_id: str
        :type traveler_id: str
        :return: A list of lists of TravelersMandatoryCheck objects.
        """
        try:
            booked_arrangements = self.db.query(BookedArrangement).filter(BookedArrangement.traveler_id == traveler_id).all()
            if booked_arrangements:
                checks = []
                for arrangement in booked_arrangements:
                    checks.append(
                        self.db.query(TravelersMandatoryCheck).filter(TravelersMandatoryCheck.booked_arrangement_id == arrangement.id).all()
                    )
                return checks
            raise BookedArrangementNotFoundException(
                code=400, message=f"Traveler with ID {traveler_id} does not have any booked arrangements."
            )
        except Exception as e:
            raise e

    def get_all_fulfilled_mandatory_checks(self):
        """
        It returns all the fulfilled mandatory checks for a traveler
        :return: A list of all the fulfilled mandatory checks.
        """
        try:
            checks = self.db.query(TravelersMandatoryCheck).filter(TravelersMandatoryCheck.is_fulfilled == True).all()
            return checks
        except Exception as e:
            raise e

    def get_all_unfulfilled_mandatory_checks(self):
        """
        It returns all the unfulfilled mandatory checks for a traveler
        :return: A list of all the unfulfilled mandatory checks.
        """
        try:
            checks = self.db.query(TravelersMandatoryCheck).filter(TravelersMandatoryCheck.is_fulfilled == False).all()
            return checks
        except Exception as e:
            raise e

    def get_travelers_mandatory_check_by_id(self, check_id: str):
        """
        It gets a TravelersMandatoryCheck object from the database by its id

        :param check_id: The ID of the check you want to retrieve
        :type check_id: str
        :return: A list of TravelersMandatoryCheck objects
        """
        try:
            check = self.db.query(TravelersMandatoryCheck).filter(TravelersMandatoryCheck.id == check_id).first()
            return check
        except Exception as e:
            raise e

    def update_mandatory_check(self, check_id: str, is_fulfilled: bool):
        """
        It updates the is_fulfilled column of the TravelersMandatoryCheck table with the value of is_fulfilled

        :param check_id: str
        :type check_id: str
        :param is_fulfilled: bool
        :type is_fulfilled: bool
        :return: The check object
        """
        try:
            check = self.db.query(TravelersMandatoryCheck).filter(TravelersMandatoryCheck.id == check_id).first()
            check.is_fulfilled = is_fulfilled
            self.db.add(check)
            self.db.commit()
            self.db.refresh(check)
            return check
        except Exception as e:
            raise e

    def delete_mandatory_check_by_id(self, check_id: str):
        """
        It deletes a mandatory check from the database

        :param check_id: str
        :type check_id: str
        :return: A boolean value.
        """
        try:
            check = self.db.query(TravelersMandatoryCheck).filter(TravelersMandatoryCheck.id == check_id).first()
            if check:
                self.db.delete(check)
                self.db.commit()
                return True
            return False
        except Exception as e:
            raise e
