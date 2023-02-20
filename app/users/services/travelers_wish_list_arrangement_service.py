from sqlalchemy.exc import IntegrityError

from app.database.db import SessionLocal

from app.users.repository.travelers_wish_list_arrangement_repository import WishListForArrangementsRepository
from app.users.exceptions.exceptions import WishListArrangementAlreadyExistsException, WishListArrangementNotFoundException


class WishListForArrangementsService:

    @staticmethod
    def create_travelers_wish_list_arrangement(arrangement_id: str, traveler_id: str):
        try:
            with SessionLocal() as db:
                wish_list_for_arrangement_repository = WishListForArrangementsRepository(db)
                return wish_list_for_arrangement_repository.create_travelers_wish_list_arrangement(arrangement_id=arrangement_id, traveler_id=traveler_id)
        except IntegrityError:
            raise WishListArrangementAlreadyExistsException(code=400, message=f"This arrangement is already in wish list for traveler with ID {traveler_id}.")
        except Exception as e:
            raise e

    @staticmethod
    def get_travelers_wish_list_arrangements(traveler_id: str):
        try:
            with SessionLocal() as db:
                wish_list_for_arrangement_repository = WishListForArrangementsRepository(db)
                wish_list_arrangements = wish_list_for_arrangement_repository.get_travelers_wish_list_arrangements(traveler_id=traveler_id)
                if wish_list_arrangements:
                    return wish_list_arrangements
                raise WishListArrangementNotFoundException(code=400, message=f"Traveler with ID {traveler_id} does not have any arrangements in wish list at the moment.")
        except Exception as e:
            raise e

    @staticmethod
    def delete_travelers_wish_list_arrangement(arrangement_id: str, traveler_id: str):
        try:
            with SessionLocal() as db:
                wish_list_for_arrangement_repository = WishListForArrangementsRepository(db)
                if wish_list_for_arrangement_repository.delete_travelers_wish_list_arrangement(arrangement_id=arrangement_id, traveler_id=traveler_id):
                    return True
                raise WishListArrangementNotFoundException(code=400, message=f"Arrangement with ID {arrangement_id} is not in wish list for traveler with ID {traveler_id}.")
        except Exception as e:
            raise e
