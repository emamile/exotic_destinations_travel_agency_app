from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.world_destinations.exceptions import StateNotFoundException, WorldDestinationNotFoundException
from app.world_destinations.service import StateService, WorldDestinationService


class StateController:
    @staticmethod
    def create_state(name: str, basic_info: str, world_destination_id: str):
        try:
            world_destination = WorldDestinationService.get_world_destination_by_id(
                world_destination_id=world_destination_id
            )
            if world_destination is None:
                raise WorldDestinationNotFoundException(
                    code=400, message=f"World destination with provided ID {world_destination_id} does not exist."
                )
            try:
                state = StateService.create_state(
                    name=name, basic_info=basic_info, world_destination_id=world_destination_id
                )
                return state
            except IntegrityError:
                raise HTTPException(status_code=400, detail=f"State with name {name} already exists.")
        except WorldDestinationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_states_for_world_destination(world_destination_id: str):
        try:
            world_destination = WorldDestinationService.get_world_destination_by_id(
                world_destination_id=world_destination_id
            )
            if world_destination is None:
                raise WorldDestinationNotFoundException(
                    code=400, message=f"World destination with provided ID {world_destination_id} does not exist."
                )
            states = StateService.get_all_states_for_world_destination(world_destination_id=world_destination_id)
            return states
        except WorldDestinationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)

    @staticmethod
    def get_state_by_id(state_id: str):
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            if state:
                return state
            else:
                raise StateNotFoundException(code=400, message=f"State with provided ID {state_id} does not exist.")
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_states_by_acronym(acronym: str):
        try:
            states = StateService.get_states_by_acronym(acronym=acronym)
            if states:
                return states
            else:
                raise StateNotFoundException(code=400, message=f"States with acronym {acronym} do not exist.")
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_state_basic_info(state_id: str, new_info: str):
        try:
            state = StateService.update_state_basic_info(state_id=state_id, new_info=new_info)
            return state
        except Exception as e:
            raise e

    @staticmethod
    def delete_state_by_id(state_id):
        try:
            if StateService.delete_state_by_id(state_id=state_id):
                return Response(content=f"State with provided ID {state_id} is deleted.", status_code=200)
            else:
                raise StateNotFoundException(code=400, message=f"State with provided ID {state_id} does not exist.")
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
