from fastapi import HTTPException, Response

from app.arrangements.exceptions.exceptions import ExcursionAlreadyExistsException, ExcursionNotFoundException
from app.arrangements.services.excursion_service import ExcursionService


# > This class is responsible for handling the user's interaction with the excursion page
class ExcursionController:
    @staticmethod
    def create_excursion(name: str, price: float, description: str):
        """
        It creates an excursion.

        :param name: str - The name of the excursion
        :type name: str
        :param price: float
        :type price: float
        :param description: The description of the excursion
        :type description: str
        :return: The excursion object
        """
        try:
            excursion = ExcursionService.create_excursion(name=name, price=price, description=description)
            return excursion
        except ExcursionAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_excursions():
        """
        It gets all the excursions
        :return: A list of all excursions
        """
        try:
            excursions = ExcursionService.get_all_excursions()
            return excursions
        except ExcursionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_excursion_by_id(excursion_id: str):
        """
        > This function gets an excursion by its id

        :param excursion_id: The id of the excursion to be retrieved
        :type excursion_id: str
        :return: The excursion object
        """
        try:
            excursion = ExcursionService.get_excursion_by_id(excursion_id=excursion_id)
            return excursion
        except ExcursionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def update_excursion_price_and_description(excursion_id: str, price: float, description: str):
        """
        > Update the price and description of an excursion

        :param excursion_id: str
        :type excursion_id: str
        :param price: float
        :type price: float
        :param description: str
        :type description: str
        :return: The excursion object
        """
        try:
            excursion = ExcursionService.get_excursion_by_id(excursion_id=excursion_id)
            return ExcursionService.update_excursion_price_and_description(excursion_id=excursion_id, price=price, description=description)
        except ExcursionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_excursion_by_id(excursion_id: str):
        """
        It deletes an excursion by its ID.

        :param excursion_id: str - the ID of the excursion to be deleted
        :type excursion_id: str
        :return: A response object with status code 200 and a message that the excursion with the given ID is deleted.
        """
        try:
            if ExcursionService.delete_excursion_by_id(excursion_id=excursion_id):
                return Response(status_code=200, content=f"Excursion with ID {excursion_id} is deleted.")
        except ExcursionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
