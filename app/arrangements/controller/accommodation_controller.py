from fastapi import HTTPException, Response

from app.arrangements.exceptions.exceptions import AccommodationAlreadyExistsException, AccommodationNotFoundException
from app.arrangements.services.accommodation_service import AccommodationService


# > This class is responsible for handling all accommodation related requests
class AccommodationController:
    @staticmethod
    def create_accommodation(name: str, type: str, description: str):
        """
        It creates an accommodation

        :param name: str - The name of the accommodation
        :type name: str
        :param type: str, description: str
        :type type: str
        :param description: str
        :type description: str
        :return: accommodation
        """
        try:
            accommodation = AccommodationService.create_accommodation(name=name, type=type, description=description)
            return accommodation
        except AccommodationAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_accommodations():
        """
        It gets all the accommodations
        :return: A list of all accommodations
        """
        try:
            accommodations = AccommodationService.get_all_accommodations()
            return accommodations
        except AccommodationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_accommodation_by_id(accommodation_id: str):
        """
        It gets an accommodation by its id.

        :param accommodation_id: The id of the accommodation to be retrieved
        :type accommodation_id: str
        :return: accommodation
        """
        try:
            accommodation = AccommodationService.get_accommodation_by_id(accommodation_id=accommodation_id)
            return accommodation
        except AccommodationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_accommodations_by_type(type: str):
        """
        It returns a list of accommodations of a given type.

        :param type: str
        :type type: str
        :return: A list of accommodations
        """
        try:
            accommodations = AccommodationService.get_accommodations_by_type(type=type)
            return accommodations
        except AccommodationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_types_of_accommodations():
        """
        It returns all types of accommodations
        :return: A list of all the types of accommodations
        """
        try:
            return AccommodationService.get_all_types_of_accommodations()
        except AccommodationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def update_accommodation_description(accommodation_id: str, description: str):
        """
        It updates the description of an accommodation.

        :param accommodation_id: The id of the accommodation to be updated
        :type accommodation_id: str
        :param description: str
        :type description: str
        :return: The accommodation object
        """
        try:
            accommodation = AccommodationService.get_accommodation_by_id(accommodation_id=accommodation_id)
            return AccommodationService.update_accommodation_description(accommodation_id=accommodation_id, description=description)
        except AccommodationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_accommodation_by_id(accommodation_id: str):
        """
        It deletes an accommodation by its ID.

        :param accommodation_id: str
        :type accommodation_id: str
        :return: A response object with a status code and a content.
        """
        try:
            if AccommodationService.delete_accommodation_by_id(accommodation_id=accommodation_id):
                return Response(status_code=200, content=f"Accommodation with ID {accommodation_id} is deleted.")
        except AccommodationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
