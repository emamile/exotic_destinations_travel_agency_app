from fastapi import HTTPException, Response

from app.users.exceptions.exceptions import TravelerAlreadyExistsException, TravelerNotFoundException, UserNotFoundException
from app.users.services.traveler_service import TravelerService
from app.users.services.user_service import UserService


# > This class is a controller for the Traveler class
class TravelerController:
    @staticmethod
    def create_traveler(name: str, surname: str, telephone_number: str, passport_number: str, user_id: str):
        """
        It creates a traveler

        :param name: str, surname: str, telephone_number: str, passport_number: str, user_id: str
        :type name: str
        :param surname: str, telephone_number: str, passport_number: str, user_id: str
        :type surname: str
        :param telephone_number: str,
        :type telephone_number: str
        :param passport_number: str,
        :type passport_number: str
        :param user_id: str
        :type user_id: str
        :return: A traveler object
        """
        try:
            user = UserService.get_user_by_id(user_id=user_id)
            traveler = TravelerService.create_traveler(
                name=name, surname=surname, telephone_number=telephone_number, passport_number=passport_number, user_id=user_id
            )
            return traveler
        except TravelerAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_travelers():
        """
        It gets all the travelers
        :return: A list of all travelers
        """
        try:
            travelers = TravelerService.get_all_travelers()
            return travelers
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_traveler_by_id(traveler_id: str):
        """
        It gets a traveler by id.

        :param traveler_id: str
        :type traveler_id: str
        :return: A traveler object
        """
        try:
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            return traveler
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_traveler_by_passport_number(passport_number: str):
        """
        It gets a traveler by passport number.

        :param passport_number: str
        :type passport_number: str
        :return: A traveler object
        """
        try:
            traveler = TravelerService.get_traveler_by_passport_number(passport_number=passport_number)
            return traveler
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def update_traveler(traveler_id: str, surname: str, telephone_number: str, passport_number: str):
        """
        It updates the traveler's information.

        :param traveler_id: str - the id of the traveler to be updated
        :type traveler_id: str
        :param surname: str,
        :type surname: str
        :param telephone_number: str, passport_number: str
        :type telephone_number: str
        :param passport_number: str
        :type passport_number: str
        :return: traveler
        """
        try:
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            traveler = TravelerService.update_traveler(
                traveler_id=traveler_id, surname=surname, telephone_number=telephone_number, passport_number=passport_number
            )
            return traveler
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_traveler_by_id(traveler_id: str):
        """
        It deletes a traveler by ID

        :param traveler_id: str
        :type traveler_id: str
        :return: a response object with a status code and a message.
        """
        try:
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            if TravelerService.delete_traveler_by_id(traveler_id=traveler_id):
                return Response(status_code=200, content=f"Traveler with ID {traveler_id} is deleted.")
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
