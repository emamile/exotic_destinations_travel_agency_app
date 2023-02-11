from app.database.db import SessionLocal
from app.world_destinations.repository import StateRepository


class StateService:
    @staticmethod
    def create_state(name: str, basic_info: str, world_destination_id: str):
        with SessionLocal() as db:
            try:
                state_repository = StateRepository(db)
                return state_repository.create_state(
                    name=name, basic_info=basic_info, world_destination_id=world_destination_id
                )
            except Exception as e:
                raise e

    @staticmethod
    def get_all_states_for_world_destination(world_destination_id: str):
        with SessionLocal() as db:
            try:
                state_repository = StateRepository(db)
                return state_repository.get_all_states_for_world_destination(world_destination_id=world_destination_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_state_by_id(state_id: str):
        with SessionLocal() as db:
            try:
                state_repository = StateRepository(db)
                return state_repository.get_state_by_id(state_id=state_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_states_by_acronym(acronym: str):
        with SessionLocal() as db:
            try:
                state_repository = StateRepository(db)
                return state_repository.get_states_by_acronym(acronym=acronym)
            except Exception as e:
                raise e

    @staticmethod
    def update_state_basic_info(state_id: str, new_info: str):
        with SessionLocal() as db:
            try:
                state_repository = StateRepository(db)
                return state_repository.update_state_basic_info(state_id=state_id, new_info=new_info)
            except Exception as e:
                raise e

    @staticmethod
    def delete_state_by_id(state_id):
        with SessionLocal() as db:
            try:
                state_repository = StateRepository(db)
                if state_repository.delete_state_by_id(state_id=state_id):
                    return True
                else:
                    return False
            except Exception as e:
                raise e
