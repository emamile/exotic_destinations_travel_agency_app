from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.world_destinations.models import WorldDestination


class WorldDestinationRepository:
    def __init__(self, database: Session):
        self.database = database

    def create_world_destination(self, name: str):
        try:
            world_destination = WorldDestination(name=name)
            self.database.add(world_destination)
            self.database.commit()
            self.database.refresh(world_destination)
            return world_destination
        except IntegrityError as e:
            raise e

    def get_all_world_destinations(self):
        world_destinations = self.database.query(WorldDestination).all()
        return world_destinations

    def get_world_destination_by_id(self, world_destination_id: str):
        world_destination = (
            self.database.query(WorldDestination).filter(WorldDestination.id == world_destination_id).first()
        )
        return world_destination

    def get_world_destinations_by_acronym(self, acronym: str):
        world_destinations = self.database.query(WorldDestination).filter(WorldDestination.name.ilike(f"%{acronym}%")).all()
        return world_destinations

    def delete_world_destination_by_id(self, world_destination_id: str):
        try:
            world_destination = (
                self.database.query(WorldDestination).filter(WorldDestination.id == world_destination_id).first()
            )
            if world_destination is None:
                return False
            self.database.delete(world_destination)
            self.database.commit()
            return True
        except Exception as e:
            raise e
