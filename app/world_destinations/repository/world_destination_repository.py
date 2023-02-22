# Importing the IntegrityError exception from the sqlalchemy.exc module.
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.world_destinations.models import WorldDestination


# > This class is responsible for retrieving and storing WorldDestination objects
class WorldDestinationRepository:
    def __init__(self, database: Session):
        self.database = database

    def create_world_destination(self, name: str):
        """
        It creates a new WorldDestination object, adds it to the database, commits the changes, and returns the new object

        :param name: str
        :type name: str
        :return: The world_destination object is being returned.
        """
        try:
            world_destination = WorldDestination(name=name)
            self.database.add(world_destination)
            self.database.commit()
            self.database.refresh(world_destination)
            return world_destination
        except IntegrityError as e:
            raise e

    def get_all_world_destinations(self):
        """
        It returns all the world destinations from the database
        :return: A list of all the world destinations in the database.
        """
        world_destinations = self.database.query(WorldDestination).all()
        return world_destinations

    def get_world_destination_by_id(self, world_destination_id: str):
        """
        This function returns a world destination object from the database based on the world destination id

        :param world_destination_id: The id of the world destination you want to get
        :type world_destination_id: str
        :return: A world destination object
        """
        """
        > This function returns a world destination object from the database based on the world destination id

        :param world_destination_id: The id of the world destination you want to get
        :type world_destination_id: str
        :return: A world destination object
        """
        world_destination = self.database.query(WorldDestination).filter(WorldDestination.id == world_destination_id).first()
        return world_destination

    def get_world_destinations_by_acronym(self, acronym: str):
        """
        > This function returns a list of WorldDestination objects that have a name that contains the acronym parameter

        :param acronym: str
        :type acronym: str
        :return: A list of WorldDestination objects
        """
        world_destinations = self.database.query(WorldDestination).filter(WorldDestination.name.ilike(f"%{acronym}%")).all()
        return world_destinations

    def delete_world_destination_by_id(self, world_destination_id: str):
        """
        Delete a world destination by id

        :param world_destination_id: The id of the world destination to delete
        :type world_destination_id: str
        :return: A boolean value.
        """
        try:
            world_destination = self.database.query(WorldDestination).filter(WorldDestination.id == world_destination_id).first()
            if world_destination is None:
                return False
            self.database.delete(world_destination)
            self.database.commit()
            return True
        except Exception as e:
            raise e
