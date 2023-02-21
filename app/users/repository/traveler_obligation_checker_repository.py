from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import CheckersNotFoundException
from app.users.models import BookedArrangement
from app.users.models.traveler_obligations_checker import TravelerObligationsChecker
from app.users.models.traveler import Traveler


class TravelerObligationCheckerRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_checkers_for_booked_arrangements(self, is_passport_valid=False, is_visa_valid=False,
                                                is_vaccine_received=False):
        try:
            booked_arrangements = self.db.query(BookedArrangement).all()
            # checkers = []
            # for arrangement in booked_arrangements:
            #     checker = TravelerObligationsChecker(is_passport_valid=is_passport_valid,
            #                                          is_visa_valid=is_visa_valid,
            #                                          is_vaccine_received=is_vaccine_received,
            #                                          arrangement_id=arrangement.arrangement_id,
            #                                          traveler_id=arrangement.traveler_id)
            #     self.db.add(checker)
            #     self.db.commit()
            #     self.db.refresh(checker)
            #     checkers.append(checkers)
            # return checkers
            existing_checkers = self.db.query(TravelerObligationsChecker).all()
            checkers = []
            if booked_arrangements:
                for arrangement in booked_arrangements:
                    if existing_checkers:
                        for check in existing_checkers:
                            if check.arrangement_id != arrangement.arrangement_id and check.traveler_id != arrangement.traveler_id:
                                checker = TravelerObligationsChecker(is_passport_valid=is_passport_valid,
                                                                     is_visa_valid=is_visa_valid,
                                                                     is_vaccine_received=is_vaccine_received,
                                                                     arrangement_id=arrangement.arrangement_id,
                                                                     traveler_id=arrangement.traveler_id)
                                self.db.add(checker)
                                self.db.commit()
                                self.db.refresh(checker)
                                checkers.append(checker)
                            else:
                                pass
                    else:
                        checker1 = TravelerObligationsChecker(is_passport_valid=is_passport_valid,
                                                              is_visa_valid=is_visa_valid,
                                                              is_vaccine_received=is_vaccine_received,
                                                              arrangement_id=arrangement.arrangement_id,
                                                              traveler_id=arrangement.traveler_id)
                        self.db.add(checker1)
                        self.db.commit()
                        self.db.refresh(checker1)
                        checkers.append(checker1)
            return checkers
        except IntegrityError as e:
            raise e

    def get_all_existing_checkers(self):
        try:
            checkers = self.db.query(TravelerObligationsChecker).all()
            return checkers
        except Exception as e:
            raise e

    def get_checkers_for_arrangement(self, arrangement_id: str):
        try:
            checkers = self.db.query(TravelerObligationsChecker).filter(
                TravelerObligationsChecker.arrangement_id == arrangement_id).first()
            return checkers
        except Exception as e:
            raise e

    def get_all_checkers_that_belong_to_traveler(self, traveler_id: str):
        try:
            checkers = self.db.query(TravelerObligationsChecker).filter(
                TravelerObligationsChecker.traveler_id == traveler_id).all()
            return checkers
        except Exception as e:
            raise e

    def get_all_travelers_that_have_all_checkers_valid(self):
        try:
            travelers = []
            checkers = self.db.query(TravelerObligationsChecker).all()
            if checkers:
                for checker in checkers:
                    if checker.is_passport_valid and checker.is_visa_valid and checker.is_vaccine_received:
                        travelers.append(self.db.query(Traveler).filter(Traveler.id == checker.traveler_id).first())
                return travelers
        except Exception as e:
            raise e

    def get_all_travelers_that_do_not_have_all_checkers_valid(self):
        try:
            travelers = []
            checkers = self.db.query(TravelerObligationsChecker).all()
            if checkers:
                for checker in checkers:
                    if not checker.is_passport_valid or not checker.is_visa_valid or not checker.is_vaccine_received:
                        travelers.append(self.db.query(Traveler).filter(Traveler.id == checker.traveler_id).first())
                return travelers
        except Exception as e:
            raise e

    def update_travelers_checker_for_arrangement(self, arrangement_id: str, traveler_id: str, is_passport_valid: bool,
                                                 is_visa_valid: bool, is_vaccine_received: bool):
        try:
            checker = self.db.query(TravelerObligationsChecker).filter(
                TravelerObligationsChecker.arrangement_id == arrangement_id and TravelerObligationsChecker.traveler_id == traveler_id).first()
            if checker:
                checker.is_passport_valid = is_passport_valid
                checker.is_visa_valid = is_visa_valid
                checker.is_vaccine_received = is_vaccine_received
                self.db.add(checker)
                self.db.commit()
                self.db.refresh(checker)
                return checker
            raise CheckersNotFoundException(code=400,
                                            message=f"Checker for arrangement with ID {arrangement_id} and traveler with ID {traveler_id} does not exist.")
        except Exception as e:
            raise e

    def delete_checker_for_traveler_and_arrangement(self, arrangement_id: str, traveler_id: str):
        try:
            checker = self.db.query(TravelerObligationsChecker).filter(
                TravelerObligationsChecker.arrangement_id == arrangement_id and TravelerObligationsChecker.traveler_id == traveler_id).first()
            if checker:
                self.db.delete(checker)
                self.db.commit()
                return True
            return False
        except Exception as e:
            raise e
