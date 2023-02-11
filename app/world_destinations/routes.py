from fastapi import APIRouter

from app.world_destinations.controller import StateController, WorldDestinationController
from app.world_destinations.schemas import StateSchema, StateSchemaIn, StateSchemaUpdate, WorldDestinationSchema, WorldDestinationSchemaIn

world_destination_router = APIRouter(tags=["WORLD DESTINATIONS"], prefix="/api/world_destinations")


@world_destination_router.post("/add-world-destination", response_model=WorldDestinationSchema)
def create_world_destination(world_destination: WorldDestinationSchemaIn):
    return WorldDestinationController.create_world_destination(name=world_destination.name)


@world_destination_router.get("/get-all-world-destinations", response_model=list[WorldDestinationSchema])
def get_all_world_destinations():
    return WorldDestinationController.get_all_world_destinations()


@world_destination_router.get("/get-world-destination-by-id", response_model=WorldDestinationSchema)
def get_world_destination_by_id(world_destination_id: str):
    return WorldDestinationController.get_world_destination_by_id(world_destination_id=world_destination_id)


@world_destination_router.get("/get-world-destination-by-acronym", response_model=list[WorldDestinationSchema])
def get_world_destination_by_acronym(acronym: str):
    return WorldDestinationController.get_world_destination_by_acronym(acronym=acronym)


@world_destination_router.delete("/delete-world-destination-by-id")
def delete_world_destination_by_id(world_destination_id: str):
    return WorldDestinationController.delete_world_destination_by_id(world_destination_id=world_destination_id)


@world_destination_router.post("/add-state-to-world-destination", response_model=StateSchema)
def create_state(state: StateSchemaIn):
    return StateController.create_state(
        name=state.name, basic_info=state.basic_info, world_destination_id=state.world_destination_id
    )


@world_destination_router.get("/get-all-states-for-world-destination", response_model=list[StateSchema])
def get_all_states_for_world_destination(world_destination_id: str):
    return StateController.get_all_states_for_world_destination(world_destination_id=world_destination_id)


@world_destination_router.get("/get-state-by-id", response_model=StateSchema)
def get_state_by_id(state_id: str):
    return StateController.get_state_by_id(state_id=state_id)


@world_destination_router.get("/get-states-by-acronym", response_model=list[StateSchema])
def get_states_by_acronym(acronym: str):
    return StateController.get_states_by_acronym(acronym=acronym)


@world_destination_router.put("/update-state-basic-info", response_model=StateSchema)
def update_state_basic_info(state: StateSchemaUpdate):
    return StateController.update_state_basic_info(state_id=state.id, new_info=state.basic_info)


@world_destination_router.get("/delete-state-by-id")
def delete_state_by_id(state_id: str):
    return StateController.delete_state_by_id(state_id=state_id)
