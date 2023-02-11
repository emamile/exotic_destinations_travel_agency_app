from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.world_destinations.exceptions import WorldDestinationNotFoundException
from app.world_destinations.service import WorldDestinationService


class WorldDestinationController:
    @staticmethod
    def create_world_destination(name: str):
        try:
            world_destination = WorldDestinationService.create_world_destination(name=name)
            return world_destination
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"World destination with name {name} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_world_destinations():
        world_destinations = WorldDestinationService.get_all_world_destinations()
        return world_destinations

    @staticmethod
    def get_world_destination_by_id(world_destination_id: str):
        try:
            world_destination = WorldDestinationService.get_world_destination_by_id(
                world_destination_id=world_destination_id
            )
            if world_destination:
                return world_destination
            else:
                raise WorldDestinationNotFoundException(
                    code=400, message=f"World destination with provided ID {world_destination_id} does not exist."
                )
        except WorldDestinationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_world_destination_by_acronym(acronym: str):
        try:
            world_destination = WorldDestinationService.get_world_destination_by_acronym(acronym=acronym)
            if world_destination:
                return world_destination
            else:
                raise WorldDestinationNotFoundException(
                    code=400, message=f"World destinations with acronym {acronym} do not exist."
                )
        except WorldDestinationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_world_destination_by_id(world_destination_id: str):
        try:
            if WorldDestinationService.delete_world_destination_by_id(world_destination_id=world_destination_id):
                return Response(
                    content=f"World destination with provided ID {world_destination_id} is deleted.", status_code=200
                )
            raise WorldDestinationNotFoundException(
                code=400, message=f"World destination with provided ID {world_destination_id} does not exist."
            )
        except WorldDestinationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
