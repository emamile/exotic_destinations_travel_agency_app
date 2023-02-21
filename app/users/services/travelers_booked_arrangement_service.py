from sqlalchemy.exc import IntegrityError

from app.database.db import SessionLocal

from app.users.repository.travelers_booked_arrangement_repository import BookedArrangementRepository
from app.users.exceptions.exceptions import BookedArrangementAlreadyExistsException, BookedArrangementNotFoundException, \
    TravelerNotFoundException


class BookedArrangementService:

    @staticmethod
    def create_travelers_booked_arrangement(arrangement_id: str, traveler_id: str):
        try:
            with SessionLocal() as db:
                booked_arrangement_repository = BookedArrangementRepository(db)
                return booked_arrangement_repository.create_travelers_booked_arrangement(arrangement_id=arrangement_id,
                                                                                         traveler_id=traveler_id)
        except IntegrityError:
            raise BookedArrangementAlreadyExistsException(code=400,
                                                          message=f"This arrangement is already booked by traveler with ID {traveler_id}.")
        except Exception as e:
            raise e

    @staticmethod
    def get_travelers_booked_arrangements(traveler_id: str):
        try:
            with SessionLocal() as db:
                booked_arrangement_repository = BookedArrangementRepository(db)
                booked_arrangements = booked_arrangement_repository.get_travelers_booked_arrangements(
                    traveler_id=traveler_id)
                if booked_arrangements:
                    return booked_arrangements
                raise BookedArrangementNotFoundException(code=400,
                                                         message=f"Traveler with ID {traveler_id} does not have any booked arrangements at the moment.")
        except Exception as e:
            raise e

    @staticmethod
    def get_all_travelers_for_booked_arrangement(arrangement_id: str):
        with SessionLocal() as db:
            try:
                booked_arrangement_repository = BookedArrangementRepository(db)
                travelers = booked_arrangement_repository.get_all_travelers_for_booked_arrangement(arrangement_id=arrangement_id)
                if travelers:
                    return travelers
                raise TravelerNotFoundException(code=400, message=f"Arrangement with provided ID {arrangement_id} is not currently booked by anyone.")
            except Exception as e:
                raise e

    @staticmethod
    def get_all_booked_arrangements():
        with SessionLocal() as db:
            try:
                booked_arrangement_repository = BookedArrangementRepository(db)
                booked_arrangements = booked_arrangement_repository.get_all_booked_arrangements()
                if booked_arrangements:
                    return booked_arrangements
                raise BookedArrangementNotFoundException(code=400, message="There are no booked arrangements at the moment.")
            except Exception as e:
                raise e

    @staticmethod
    def delete_travelers_booked_arrangement(arrangement_id: str, traveler_id: str):
        try:
            with SessionLocal() as db:
                booked_arrangement_repository = BookedArrangementRepository(db)
                if booked_arrangement_repository.delete_travelers_booked_arrangement(arrangement_id=arrangement_id,
                                                                                     traveler_id=traveler_id):
                    return True
                raise BookedArrangementNotFoundException(code=400,
                                                         message=f"Arrangement with ID {arrangement_id} is not booked by traveler with ID {traveler_id}.")
        except Exception as e:
            raise e
