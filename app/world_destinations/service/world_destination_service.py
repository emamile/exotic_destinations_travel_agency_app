from sqlalchemy.exc import IntegrityError

from app.database.db import SessionLocal
from app.world_destinations.exceptions import WorldDestinationNotFoundException, WorldDestinationAlreadyExistsException
from app.world_destinations.repository import WorldDestinationRepository


class WorldDestinationService:
    @staticmethod
    def create_world_destination(name: str):
        try:
            with SessionLocal() as db:
                world_destination_repository = WorldDestinationRepository(db)
                return world_destination_repository.create_world_destination(name=name)
        except IntegrityError:
            raise WorldDestinationAlreadyExistsException(code=400, message=f"World destination with name {name} already exists.")

    @staticmethod
    def get_all_world_destinations():
        try:
            with SessionLocal() as db:
                world_destination_repository = WorldDestinationRepository(db)
                return world_destination_repository.get_all_world_destinations()
        except Exception as e:
            raise e

    @staticmethod
    def get_world_destination_by_id(world_destination_id: str):
        try:
            with SessionLocal() as db:
                world_destination_repository = WorldDestinationRepository(db)
                world_destination = world_destination_repository.get_world_destination_by_id(
                    world_destination_id=world_destination_id
                )
                if world_destination is None:
                    raise WorldDestinationNotFoundException(code=400,
                                                            message=f"World destination with provided ID {world_destination_id} does not exist.")
                return world_destination
        except Exception as e:
            raise e

    @staticmethod
    def get_world_destinations_by_acronym(acronym: str):
        try:
            with SessionLocal() as db:
                world_destination_repository = WorldDestinationRepository(db)
                world_destinations = world_destination_repository.get_world_destinations_by_acronym(acronym=acronym)
                if world_destinations:
                    return world_destinations
                raise WorldDestinationNotFoundException(
                    code=400, message=f"World destinations with acronym {acronym} do not exist."
                )
        except Exception as e:
            raise e

    @staticmethod
    def delete_world_destination_by_id(world_destination_id: str):
        try:
            with SessionLocal() as db:
                world_destination_repository = WorldDestinationRepository(db)
                if world_destination_repository.delete_world_destination_by_id(
                    world_destination_id=world_destination_id
                ):
                    return True
                raise WorldDestinationNotFoundException(
                    code=400, message=f"World destination with provided ID {world_destination_id} does not exist.")
        except Exception as e:
            raise e
