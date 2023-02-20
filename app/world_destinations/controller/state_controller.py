from fastapi import HTTPException, Response
from app.world_destinations.exceptions import StateNotFoundException, WorldDestinationNotFoundException, StateAlreadyExistsException
from app.world_destinations.service import StateService, WorldDestinationService


class StateController:
    @staticmethod
    def create_state(name: str, basic_info: str, world_destination_id: str):
        try:
            world_destination = WorldDestinationService.get_world_destination_by_id(
                world_destination_id=world_destination_id)
            state = StateService.create_state(
                name=name, basic_info=basic_info, world_destination_id=world_destination_id)
            return state
        except StateAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except WorldDestinationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_states_for_world_destination(world_destination_id: str):
        try:
            world_destination = WorldDestinationService.get_world_destination_by_id(
                world_destination_id=world_destination_id)
            states = StateService.get_all_states_for_world_destination(world_destination_id=world_destination_id)
            return states
        except WorldDestinationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_state_by_id(state_id: str):
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            return state
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_states_by_acronym(acronym: str):
        try:
            states = StateService.get_states_by_acronym(acronym=acronym)
            return states
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_state_basic_info(state_id: str, new_info: str):
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            state = StateService.update_state_basic_info(state_id=state_id, new_info=new_info)
            return state
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def delete_state_by_id(state_id):
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            if StateService.delete_state_by_id(state_id=state_id):
                return Response(content=f"State with provided ID {state_id} is deleted.", status_code=200)
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
