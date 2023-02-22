# Importing the APIRouter and Depends classes from the fastapi module.
from fastapi import APIRouter, Depends

from app.users.controller.user_auth_handler_controller import JWTBearer
from app.world_destinations.controller import StateController, StateInfoController, WorldDestinationController
from app.world_destinations.schemas import (
    StateInfoSchema,
    StateInfoSchemaIn,
    StateInfoSchemaUpdate,
    StateSchema,
    StateSchemaIn,
    StateSchemaUpdate,
    WorldDestinationSchema,
    WorldDestinationSchemaIn,
)

world_destination_router = APIRouter(tags=["WORLD DESTINATIONS"], prefix="/api/world_destinations")
state_router = APIRouter(tags=["STATES"], prefix="/api/states")


@world_destination_router.post(
    "/add-world-destination", response_model=WorldDestinationSchema, dependencies=[Depends(JWTBearer("superuser"))]
)
def create_world_destination(world_destination: WorldDestinationSchemaIn):
    """
    `create_world_destination` creates a new world destination

    :param world_destination: WorldDestinationSchemaIn
    :type world_destination: WorldDestinationSchemaIn
    :return: A WorldDestination object
    """
    return WorldDestinationController.create_world_destination(name=world_destination.name)


@world_destination_router.get("/get-all-world-destinations", response_model=list[WorldDestinationSchema])
def get_all_world_destinations():
    """
    > Get all world destinations
    :return: A list of all the world destinations
    """
    return WorldDestinationController.get_all_world_destinations()


@world_destination_router.get(
    "/get-world-destination-by-id", response_model=WorldDestinationSchema, dependencies=[Depends(JWTBearer("superuser"))]
)
def get_world_destination_by_id(world_destination_id: str):
    """
    Get a world destination by its id

    :param world_destination_id: The id of the world destination you want to get
    :type world_destination_id: str
    :return: A WorldDestination object
    """
    return WorldDestinationController.get_world_destination_by_id(world_destination_id=world_destination_id)


@world_destination_router.get("/get-world-destinations-by-acronym", response_model=list[WorldDestinationSchema])
def get_world_destinations_by_acronym(acronym: str):
    """
    `get_world_destinations_by_acronym` returns a list of world destinations that match the given acronym

    :param acronym: str
    :type acronym: str
    :return: A list of WorldDestination objects
    """
    return WorldDestinationController.get_world_destinations_by_acronym(acronym=acronym)


@world_destination_router.delete("/delete-world-destination-by-id", dependencies=[Depends(JWTBearer("superuser"))])
def delete_world_destination_by_id(world_destination_id: str):
    """
    Delete a world destination by id

    :param world_destination_id: str
    :type world_destination_id: str
    :return: A dictionary with the following keys:
        - status: 200
        - message: "Successfully deleted world destination with id: <world_destination_id>"
        - world_destination: The world destination that was deleted
    """
    return WorldDestinationController.delete_world_destination_by_id(world_destination_id=world_destination_id)


@state_router.post("/add-state-to-world-destination", response_model=StateSchema, dependencies=[Depends(JWTBearer("superuser"))])
def create_state(state: StateSchemaIn):
    """
    `create_state` creates a new state

    :param state: StateSchemaIn
    :type state: StateSchemaIn
    :return: The state that was created.
    """
    return StateController.create_state(name=state.name, basic_info=state.basic_info, world_destination_id=state.world_destination_id)


@state_router.get("/get-all-states-for-world-destination", response_model=list[StateSchema])
def get_all_states_for_world_destination(world_destination_id: str):
    """
    Get all states for a world destination

    :param world_destination_id: The id of the world destination you want to get all states for
    :type world_destination_id: str
    :return: A list of all the states for a given world destination.
    """
    return StateController.get_all_states_for_world_destination(world_destination_id=world_destination_id)


@state_router.get("/get-state-by-id", response_model=StateSchema, dependencies=[Depends(JWTBearer("superuser"))])
def get_state_by_id(state_id: str):
    """
    `get_state_by_id` returns a state object given a state id

    :param state_id: The id of the state you want to get
    :type state_id: str
    :return: A state object
    """
    return StateController.get_state_by_id(state_id=state_id)


@state_router.get("/get-states-by-acronym", response_model=list[StateSchema])
def get_states_by_acronym(acronym: str):
    """
    `get_states_by_acronym` returns a list of states that match the given acronym

    :param acronym: The acronym of the state you want to search for
    :type acronym: str
    :return: A list of states that match the acronym.
    """
    return StateController.get_states_by_acronym(acronym=acronym)


@state_router.put("/update-state-basic-info", response_model=StateSchema, dependencies=[Depends(JWTBearer("superuser"))])
def update_state_basic_info(state: StateSchemaUpdate):
    """
    `update_state_basic_info` updates the basic info of a state

    :param state: StateSchemaUpdate
    :type state: StateSchemaUpdate
    :return: The updated state.
    """
    return StateController.update_state_basic_info(state_id=state.id, new_info=state.basic_info)


@state_router.get("/delete-state-by-id", dependencies=[Depends(JWTBearer("superuser"))])
def delete_state_by_id(state_id: str):
    """
    Delete a state by id

    :param state_id: The id of the state to delete
    :type state_id: str
    :return: The return value is the result of the delete_state_by_id function in the StateController class.
    """
    return StateController.delete_state_by_id(state_id=state_id)


@state_router.post("/add-state-info", response_model=StateInfoSchema, dependencies=[Depends(JWTBearer("superuser"))])
def add_state_info(info: StateInfoSchemaIn):
    """
    `add_state_info` creates a new state info

    :param info: StateInfoSchemaIn - this is the input parameter that is passed to the function
    :type info: StateInfoSchemaIn
    :return: The return value is a StateInfo object.
    """
    return StateInfoController.create_state_info(
        info_title=info.info_title, details=info.details, state_id=info.state_id, is_mandatory=info.is_mandatory
    )


@state_router.get("/get-state-infos", response_model=list[StateInfoSchema])
def get_state_infos(state_id: str):
    """
    > Get the state information for a given state ID

    :param state_id: The state id of the state you want to get the state info of
    :type state_id: str
    :return: A list of StateInfo objects
    """
    return StateInfoController.get_state_infos(state_id=state_id)


@state_router.get("/get-state-info-by-info-title", response_model=StateInfoSchema)
def get_state_info_by_info_title(state_id: str, info_title: str):
    """
    > Get a state info by state id and info title

    :param state_id: The id of the state you want to get the info from
    :type state_id: str
    :param info_title: The title of the information you want to get
    :type info_title: str
    :return: A list of StateInfo objects
    """
    return StateInfoController.get_state_info_by_info_title(state_id=state_id, info_title=info_title)


@state_router.get("/get-all-mandatory-state-infos", response_model=list[StateInfoSchema])
def get_all_mandatory_state_infos(state_id: str):
    """
    Get all mandatory state infos for a given state

    :param state_id: The id of the state you want to get the mandatory state infos for
    :type state_id: str
    :return: A list of all mandatory state infos for a given state.
    """
    return StateInfoController.get_all_mandatory_state_infos(state_id=state_id)


@state_router.put("/update-state-info", response_model=StateInfoSchema, dependencies=[Depends(JWTBearer("superuser"))])
def update_state_info(info: StateInfoSchemaUpdate):
    """
    Update the state info with the given id

    :param info: StateInfoSchemaUpdate
    :type info: StateInfoSchemaUpdate
    :return: The updated state info object.
    """
    return StateInfoController.update_state_info(state_info_id=info.id, details=info.details, is_mandatory=info.is_mandatory)


@state_router.delete("/delete-state-info-by-id", dependencies=[Depends(JWTBearer("superuser"))])
def delete_state_info_by_id(state_info_id: str):
    """
    Delete a state info by id

    :param state_info_id: str
    :type state_info_id: str
    :return: The state_info_id of the state_info that was deleted.
    """
    return StateInfoController.delete_state_info_by_id(state_info_id=state_info_id)
