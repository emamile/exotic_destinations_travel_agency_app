# Importing the IntegrityError exception from the sqlalchemy.exc module.
from sqlalchemy.exc import IntegrityError

from app.database.db import SessionLocal
from app.world_destinations.exceptions import StateAlreadyExistsException, StateNotFoundException
from app.world_destinations.repository import StateRepository


# > This class is responsible for managing the state of the application
class StateService:
    @staticmethod
    def create_state(name: str, basic_info: str, world_destination_id: str):
        """
        It creates a state in the database

        :param name: str
        :type name: str
        :param basic_info: str = "This is a basic info"
        :type basic_info: str
        :param world_destination_id: This is the id of the world destination that the state belongs to
        :type world_destination_id: str
        :return: The state object that was created.
        """
        try:
            with SessionLocal() as db:
                state_repository = StateRepository(db)
                return state_repository.create_state(name=name, basic_info=basic_info, world_destination_id=world_destination_id)
        except IntegrityError as exc:
            raise StateAlreadyExistsException(
                code=409, message=f"State with name {name} for this world destination already exists."
            ) from exc
        except Exception as e:
            raise e

    @staticmethod
    def get_all_states_for_world_destination(world_destination_id: str):
        """
        It gets all states for a world destination

        :param world_destination_id: The ID of the world destination you want to get all states for
        :type world_destination_id: str
        :return: A list of states for a given world destination.
        """
        try:
            with SessionLocal() as db:
                state_repository = StateRepository(db)
                states = state_repository.get_all_states_for_world_destination(world_destination_id=world_destination_id)
                if states:
                    return states
                raise StateNotFoundException(code=400, message=f"World destination with ID {world_destination_id} currently has no states.")
        except Exception as e:
            raise e

    @staticmethod
    def get_state_by_id(state_id: str):
        """
        > This function gets a state by its ID

        :param state_id: The ID of the state you want to get
        :type state_id: str
        :return: A state object
        """
        try:
            with SessionLocal() as db:
                state_repository = StateRepository(db)
                state = state_repository.get_state_by_id(state_id=state_id)
                if state:
                    return state
                raise StateNotFoundException(code=400, message=f"State with provided ID {state_id} does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def get_states_by_acronym(acronym: str):
        """
        It gets a list of states by acronym

        :param acronym: str
        :type acronym: str
        :return: A list of states with the acronym passed as parameter.
        """
        try:
            with SessionLocal() as db:
                state_repository = StateRepository(db)
                states = state_repository.get_states_by_acronym(acronym=acronym)
                if states:
                    return states
                raise StateNotFoundException(code=400, message=f"States with acronym {acronym} do not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def update_state_basic_info(state_id: str, new_info: str):
        """
        It takes a state_id and new_info as arguments, and updates the state's basic info with the new_info

        :param state_id: The id of the state you want to update
        :type state_id: str
        :param new_info: str
        :type new_info: str
        :return: The updated state object
        """
        try:
            with SessionLocal() as db:
                state_repository = StateRepository(db)
                return state_repository.update_state_basic_info(state_id=state_id, new_info=new_info)
        except Exception as e:
            raise e

    @staticmethod
    def delete_state_by_id(state_id: str):
        """
        It deletes a state by its ID.

        :param state_id: The ID of the state to be deleted
        :type state_id: str
        :return: A boolean value.
        """
        try:
            with SessionLocal() as db:
                state_repository = StateRepository(db)
                if state_repository.delete_state_by_id(state_id=state_id):
                    return True
                raise StateNotFoundException(code=400, message=f"State with provided ID {state_id} does not exist.")
        except Exception as e:
            raise e
