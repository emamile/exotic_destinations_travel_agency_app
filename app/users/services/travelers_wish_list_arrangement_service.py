# Importing the IntegrityError exception from the sqlalchemy library.
from sqlalchemy.exc import IntegrityError

from app.database.db import SessionLocal
from app.users.exceptions.exceptions import WishListArrangementAlreadyExistsException, WishListArrangementNotFoundException
from app.users.repository.travelers_wish_list_arrangement_repository import WishListForArrangementsRepository


# > This class is responsible for managing the wish list for arrangements
class WishListForArrangementsService:
    @staticmethod
    def create_travelers_wish_list_arrangement(arrangement_id: str, traveler_id: str):
        """
        It creates a new wish list arrangement for a traveler

        :param arrangement_id: str
        :type arrangement_id: str
        :param traveler_id: str
        :type traveler_id: str
        :return: The wish list for arrangement object.
        """
        try:
            with SessionLocal() as db:
                wish_list_for_arrangement_repository = WishListForArrangementsRepository(db)
                return wish_list_for_arrangement_repository.create_travelers_wish_list_arrangement(
                    arrangement_id=arrangement_id, traveler_id=traveler_id
                )
        except IntegrityError as exc:
            raise WishListArrangementAlreadyExistsException(
                code=409, message=f"This arrangement is already in wish list for traveler with ID {traveler_id}."
            ) from exc
        except Exception as e:
            raise e

    @staticmethod
    def get_travelers_wish_list_arrangements(traveler_id: str):
        """
        It gets the wish list arrangements for a traveler with a given ID

        :param traveler_id: str
        :type traveler_id: str
        :return: A list of wish list arrangements for a traveler.
        """
        try:
            with SessionLocal() as db:
                wish_list_for_arrangement_repository = WishListForArrangementsRepository(db)
                wish_list_arrangements = wish_list_for_arrangement_repository.get_travelers_wish_list_arrangements(traveler_id=traveler_id)
                if wish_list_arrangements:
                    return wish_list_arrangements
                raise WishListArrangementNotFoundException(
                    code=400, message=f"Traveler with ID {traveler_id} does not have any arrangements in wish list at the moment."
                )
        except Exception as e:
            raise e

    @staticmethod
    def delete_travelers_wish_list_arrangement(arrangement_id: str, traveler_id: str):
        """
        It deletes a wish list arrangement for a traveler

        :param arrangement_id: str
        :type arrangement_id: str
        :param traveler_id: str
        :type traveler_id: str
        :return: True or False
        """
        try:
            with SessionLocal() as db:
                wish_list_for_arrangement_repository = WishListForArrangementsRepository(db)
                if wish_list_for_arrangement_repository.delete_travelers_wish_list_arrangement(
                    arrangement_id=arrangement_id, traveler_id=traveler_id
                ):
                    return True
                raise WishListArrangementNotFoundException(
                    code=400, message=f"Arrangement with ID {arrangement_id} is not in wish list for traveler with ID {traveler_id}."
                )
        except Exception as e:
            raise e
