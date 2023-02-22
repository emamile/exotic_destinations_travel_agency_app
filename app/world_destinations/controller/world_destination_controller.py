# Importing the HTTPException and Response classes from the fastapi module.
from fastapi import HTTPException, Response

from app.world_destinations.exceptions import WorldDestinationAlreadyExistsException, WorldDestinationNotFoundException
from app.world_destinations.service import WorldDestinationService


# > This class is responsible for handling all the requests related to the WorldDestination model
class WorldDestinationController:
    @staticmethod
    def create_world_destination(name: str):
        """
        It creates a world destination.

        :param name: str
        :type name: str
        :return: A WorldDestination object
        """
        try:
            world_destination = WorldDestinationService.create_world_destination(name=name)
            return world_destination
        except WorldDestinationAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_world_destinations():
        try:
            world_destinations = WorldDestinationService.get_all_world_destinations()
            return world_destinations
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_world_destination_by_id(world_destination_id: str):
        try:
            world_destination = WorldDestinationService.get_world_destination_by_id(world_destination_id=world_destination_id)
            return world_destination
        except WorldDestinationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_world_destinations_by_acronym(acronym: str):
        try:
            world_destinations = WorldDestinationService.get_world_destinations_by_acronym(acronym=acronym)
            return world_destinations
        except WorldDestinationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_world_destination_by_id(world_destination_id: str):
        try:
            if WorldDestinationService.delete_world_destination_by_id(world_destination_id=world_destination_id):
                return Response(content=f"World destination with provided ID {world_destination_id} is deleted.", status_code=200)
        except WorldDestinationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
