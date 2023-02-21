from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.world_destinations.models.state import State


class StateRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_state(self, name: str, basic_info: str, world_destination_id: str):
        try:
            state = State(name=name, basic_info=basic_info, world_destination_id=world_destination_id)
            self.db.add(state)
            self.db.commit()
            self.db.refresh(state)
            return state
        except IntegrityError as e:
            raise e

    def get_all_states_for_world_destination(self, world_destination_id: str):
        try:
            states = self.db.query(State).filter(State.world_destination_id == world_destination_id).all()
            return states
        except Exception as e:
            raise e

    def get_state_by_id(self, state_id: str):
        state = self.db.query(State).filter(State.id == state_id).first()
        return state

    def get_states_by_acronym(self, acronym: str):
        try:
            states = self.db.query(State).filter(State.name.ilike(f"%{acronym}%")).all()
            return states
        except Exception as e:
            raise e

    def update_state_basic_info(self, state_id: str, new_info: str):
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
        try:
            state = self.db.query(State).filter(State.id == state_id).first()
            if state is None:
                return False
            self.db.delete(state)
            self.db.commit()
            return True
        except Exception as e:
            raise e
