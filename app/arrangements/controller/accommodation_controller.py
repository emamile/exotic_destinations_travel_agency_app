from fastapi import HTTPException, Response
from app.arrangements.exceptions.exceptions import AccommodationNotFoundException, AccommodationAlreadyExistsException
from app.arrangements.services.accommodation_service import AccommodationService


class AccommodationController:

    @staticmethod
    def create_accommodation(name: str, accommodation_type: str, description: str):
        try:
            accommodation = AccommodationService.create_accommodation(name=name, accommodation_type=accommodation_type, description=description)
            return accommodation
        except AccommodationAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_accommodations():
        try:
            accommodations = AccommodationService.get_all_accommodations()
            return accommodations
        except AccommodationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_accommodation_by_id(accommodation_id: str):
        try:
            accommodation = AccommodationService.get_accommodation_by_id(accommodation_id=accommodation_id)
            return accommodation
        except AccommodationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_accommodations_by_type(type: str):
        try:
            accommodations = AccommodationService.get_accommodations_by_type(type=type)
            return accommodations
        except AccommodationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_types_of_accommodations():
        try:
            return AccommodationService.get_all_types_of_accommodations()
        except AccommodationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_accommodation_description(accommodation_id: str, description: str):
        try:
            accommodation = AccommodationService.get_accommodation_by_id(accommodation_id=accommodation_id)
            return AccommodationService.update_accommodation_description(accommodation_id=accommodation_id, description=description)
        except AccommodationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_accommodation_by_id(accommodation_id: str):
        try:
            if AccommodationService.delete_accommodation_by_id(accommodation_id=accommodation_id):
                return Response(status_code=200, content=f"Accommodation with ID {accommodation_id} is deleted.")
        except AccommodationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
