from fastapi import HTTPException, Response
from app.arrangements.exceptions.exceptions import ExcursionNotFoundException, ExcursionAlreadyExistsException
from app.arrangements.services.excursion_service import ExcursionService


class ExcursionController:

    @staticmethod
    def create_excursion(name: str, price: float, description: str):
        try:
            excursion = ExcursionService.create_excursion(name=name, price=price, description=description)
            return excursion
        except ExcursionAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_excursions():
        try:
            excursions = ExcursionService.get_all_excursions()
            return excursions
        except ExcursionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_excursion_by_id(excursion_id: str):
        try:
            excursion = ExcursionService.get_excursion_by_id(excursion_id=excursion_id)
            return excursion
        except ExcursionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_excursion_price_and_description(excursion_id: str, price: float, description: str):
        try:
            excursion = ExcursionService.get_excursion_by_id(excursion_id=excursion_id)
            return ExcursionService.update_excursion_price_and_description(excursion_id=excursion_id, price=price, description=description)
        except ExcursionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_excursion_by_id(excursion_id: str):
        try:
            if ExcursionService.delete_excursion_by_id(excursion_id=excursion_id):
                return Response(status_code=200, content=f"Excursion with ID {excursion_id} is deleted.")
        except ExcursionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
