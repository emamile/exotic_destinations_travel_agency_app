from fastapi import HTTPException, Response
from app.users.services.traveler_service import TravelerService
from app.users.exceptions.exceptions import TravelerNotFoundException, UserNotFoundException, \
    TravelerAlreadyExistsException
from app.users.services.user_service import UserService


class TravelerController:

    @staticmethod
    def create_traveler(name: str, surname: str, telephone_number: str, passport_number: str, user_id: str):
        try:
            user = UserService.get_user_by_id(user_id=user_id)
            traveler = TravelerService.create_traveler(name=name, surname=surname, telephone_number=telephone_number,
                                                       passport_number=passport_number, user_id=user_id)
            return traveler
        except TravelerAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_travelers():
        try:
            travelers = TravelerService.get_all_travelers()
            return travelers
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_traveler_by_id(traveler_id: str):
        try:
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            return traveler
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_traveler_by_passport_number(passport_number: str):
        try:
            traveler = TravelerService.get_traveler_by_passport_number(passport_number=passport_number)
            return traveler
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_traveler(traveler_id: str, surname: str, telephone_number: str, passport_number: str):
        try:
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            traveler = TravelerService.update_traveler(traveler_id=traveler_id, surname=surname,
                                                       telephone_number=telephone_number,
                                                       passport_number=passport_number)
            return traveler
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_traveler_by_id(traveler_id: str):
        try:
            traveler = TravelerService.get_traveler_by_id(traveler_id=traveler_id)
            if TravelerService.delete_traveler_by_id(traveler_id=traveler_id):
                return Response(status_code=200, content=f"Traveler with ID {traveler_id} is deleted.")
        except TravelerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
