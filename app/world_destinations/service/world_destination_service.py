# Importing the IntegrityError exception from the sqlalchemy library.
from sqlalchemy.exc import IntegrityError

from app.database.db import SessionLocal
from app.world_destinations.exceptions import WorldDestinationAlreadyExistsException, WorldDestinationNotFoundException
from app.world_destinations.repository import WorldDestinationRepository


# > This class is responsible for providing a list of world destinations
class WorldDestinationService:
    @staticmethod
    def create_world_destination(name: str):
        """
        > Create a new world destination with the given name

        :param name: str
        :type name: str
        :return: The world destination object
        """
        try:
            with SessionLocal() as db:
                world_destination_repository = WorldDestinationRepository(db)
                return world_destination_repository.create_world_destination(name=name)
        except IntegrityError as exc:
            raise WorldDestinationAlreadyExistsException(code=409, message=f"World destination with name {name} already exists.") from exc

    @staticmethod
    def get_all_world_destinations():
        """
        It gets all the world destinations from the database
        :return: A list of all the world destinations
        """
        try:
            with SessionLocal() as db:
                world_destination_repository = WorldDestinationRepository(db)
                return world_destination_repository.get_all_world_destinations()
        except Exception as e:
            raise e

    @staticmethod
    def get_world_destination_by_id(world_destination_id: str):
        """
        It gets a world destination by its ID

        :param world_destination_id: The ID of the world destination you want to get
        :type world_destination_id: str
        :return: A world destination object.
        """
        try:
            with SessionLocal() as db:
                world_destination_repository = WorldDestinationRepository(db)
                world_destination = world_destination_repository.get_world_destination_by_id(world_destination_id=world_destination_id)
                if world_destination is None:
                    raise WorldDestinationNotFoundException(
                        code=400, message=f"World destination with provided ID {world_destination_id} does not exist."
                    )
                return world_destination
        except Exception as e:
            raise e

    @staticmethod
    def get_world_destinations_by_acronym(acronym: str):
        """
        It gets a list of world destinations by acronym

        :param acronym: str
        :type acronym: str
        :return: A list of world destinations
        """
        try:
            with SessionLocal() as db:
                world_destination_repository = WorldDestinationRepository(db)
                world_destinations = world_destination_repository.get_world_destinations_by_acronym(acronym=acronym)
                if world_destinations:
                    return world_destinations
                raise WorldDestinationNotFoundException(code=400, message=f"World destinations with acronym {acronym} do not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def delete_world_destination_by_id(world_destination_id: str):
        """
        It deletes a world destination by ID

        :param world_destination_id: str
        :type world_destination_id: str
        :return: A boolean value.
        """
        try:
            with SessionLocal() as db:
                world_destination_repository = WorldDestinationRepository(db)
                if world_destination_repository.delete_world_destination_by_id(world_destination_id=world_destination_id):
                    return True
                raise WorldDestinationNotFoundException(
                    code=400, message=f"World destination with provided ID {world_destination_id} does not exist."
                )
        except Exception as e:
            raise e
