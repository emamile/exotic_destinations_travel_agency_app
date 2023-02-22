# Importing the IntegrityError exception from the sqlalchemy.exc module.
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.world_destinations.models.state import State


# > This class is responsible for storing and retrieving the state of the game
class StateRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_state(self, name: str, basic_info: str, world_destination_id: str):
        """
        It creates a new state in the database

        :param name: str
        :type name: str
        :param basic_info: This is a string that contains the basic information about the state
        :type basic_info: str
        :param world_destination_id: This is the id of the world destination that the state belongs to
        :type world_destination_id: str
        :return: The state object
        """
        try:
            state = State(name=name, basic_info=basic_info, world_destination_id=world_destination_id)
            self.db.add(state)
            self.db.commit()
            self.db.refresh(state)
            return state
        except IntegrityError as e:
            raise e

    def get_all_states_for_world_destination(self, world_destination_id: str):
        """
        It returns all the states for a given world destination

        :param world_destination_id: The id of the world destination you want to get all states for
        :type world_destination_id: str
        :return: A list of all the states in the database.
        """
        try:
            states = self.db.query(State).filter(State.world_destination_id == world_destination_id).all()
            return states
        except Exception as e:
            raise e

    def get_state_by_id(self, state_id: str):
        """
        It returns the state object with the given id.

        :param state_id: The id of the state you want to get
        :type state_id: str
        :return: The state object
        """
        state = self.db.query(State).filter(State.id == state_id).first()
        return state

    def get_states_by_acronym(self, acronym: str):
        """
        This function takes in a string as an argument and returns a list of objects that match the string

        :param acronym: str
        :type acronym: str
        :return: A list of objects of type State
        """
        try:
            states = self.db.query(State).filter(State.name.ilike(f"%{acronym}%")).all()
            return states
        except Exception as e:
            raise e

    def update_state_basic_info(self, state_id: str, new_info: str):
        """
        It takes a state_id and a new_info string, and updates the basic_info field of the state with the given state_id

        :param state_id: The id of the state you want to update
        :type state_id: str
        :param new_info: str
        :type new_info: str
        :return: The state object
        """
        try:
            state = self.db.query(State).filter(State.id == state_id).first()
            state.basic_info = new_info
            self.db.add(state)
            self.db.commit()
            self.db.refresh(state)
            return state
        except Exception as e:
            raise e

    def delete_state_by_id(self, state_id: str):
        """
        It deletes a state from the database by its id

        :param state_id: The id of the state to be deleted
        :type state_id: str
        :return: A boolean value.
        """
        try:
            state = self.db.query(State).filter(State.id == state_id).first()
            if state is None:
                return False
            self.db.delete(state)
            self.db.commit()
            return True
        except Exception as e:
            raise e
