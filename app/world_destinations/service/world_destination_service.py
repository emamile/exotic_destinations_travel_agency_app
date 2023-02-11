from app.database.db import SessionLocal
from app.world_destinations.repository import WorldDestinationRepository


class WorldDestinationService:
    @staticmethod
    def create_world_destination(name: str):
        with SessionLocal() as db:
            try:
                world_destination_repository = WorldDestinationRepository(db)
                return world_destination_repository.create_world_destination(name=name)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_world_destinations():
        with SessionLocal() as db:
            try:
                world_destination_repository = WorldDestinationRepository(db)
                return world_destination_repository.get_all_world_destinations()
            except Exception as e:
                raise e

    @staticmethod
    def get_world_destination_by_id(world_destination_id: str):
        with SessionLocal() as db:
            try:
                world_destination_repository = WorldDestinationRepository(db)
                return world_destination_repository.get_world_destination_by_id(
                    world_destination_id=world_destination_id
                )
            except Exception as e:
                raise e

    @staticmethod
    def get_world_destination_by_acronym(acronym: str):
        with SessionLocal() as db:
            try:
                world_destination_repository = WorldDestinationRepository(db)
                return world_destination_repository.get_world_destination_by_acronym(acronym=acronym)
            except Exception as e:
                raise e

    @staticmethod
    def delete_world_destination_by_id(world_destination_id: str):
        with SessionLocal() as db:
            try:
                world_destination_repository = WorldDestinationRepository(db)
                if world_destination_repository.delete_world_destination_by_id(
                    world_destination_id=world_destination_id
                ):
                    return True
                else:
                    return False
            except Exception as e:
                raise e
