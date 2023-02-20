from sqlalchemy.exc import IntegrityError

from app.database.db import SessionLocal
from app.world_destinations.exceptions import StateNotFoundException, StateAlreadyExistsException
from app.world_destinations.repository import StateRepository


class StateService:
    @staticmethod
    def create_state(name: str, basic_info: str, world_destination_id: str):
        try:
            with SessionLocal() as db:
                state_repository = StateRepository(db)
                return state_repository.create_state(
                    name=name, basic_info=basic_info, world_destination_id=world_destination_id
                )
        except IntegrityError:
            raise StateAlreadyExistsException(code=400, message=f"State with name {name} for this world destination already exists.")
        except Exception as e:
            raise e

    @staticmethod
    def get_all_states_for_world_destination(world_destination_id: str):
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
        try:
            with SessionLocal() as db:
                state_repository = StateRepository(db)
                return state_repository.update_state_basic_info(state_id=state_id, new_info=new_info)
        except Exception as e:
            raise e

    @staticmethod
    def delete_state_by_id(state_id: str):
        try:
            with SessionLocal() as db:
                state_repository = StateRepository(db)
                if state_repository.delete_state_by_id(state_id=state_id):
                    return True
                raise StateNotFoundException(code=400, message=f"State with provided ID {state_id} does not exist.")
        except Exception as e:
            raise e
