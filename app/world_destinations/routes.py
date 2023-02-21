from fastapi import APIRouter

from app.world_destinations.controller import StateController, WorldDestinationController, \
    UsefulInfoAboutStateController
from app.world_destinations.schemas import StateSchema, StateSchemaIn, StateSchemaUpdate, WorldDestinationSchema, \
    WorldDestinationSchemaIn, UsefulInfoAboutStateSchema, UsefulInfoAboutStateSchemaIn

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


@world_destination_router.get("/get-world-destinations-by-acronym", response_model=list[WorldDestinationSchema])
def get_world_destinations_by_acronym(acronym: str):
    return WorldDestinationController.get_world_destinations_by_acronym(acronym=acronym)


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


@world_destination_router.post("/add-state's-useful-information", response_model=UsefulInfoAboutStateSchema)
def add_states_useful_information(useful_info: UsefulInfoAboutStateSchemaIn):
    return UsefulInfoAboutStateController.create_states_useful_info(info_title=useful_info.info_title,
                                                                    details=useful_info.details,
                                                                    state_id=useful_info.state_id)


@world_destination_router.get("/get-state's-useful-informations", response_model=list[UsefulInfoAboutStateSchema])
def get_states_useful_informations(state_id: str):
    return UsefulInfoAboutStateController.get_states_useful_infos(state_id=state_id)


@world_destination_router.get("/get-state's-useful-information-by-info-title",
                              response_model=UsefulInfoAboutStateSchema)
def get_states_useful_information_by_info_title(state_id: str, info_title: str):
    return UsefulInfoAboutStateController.get_states_useful_info_by_info_title(state_id=state_id, info_title=info_title)


@world_destination_router.put("/update-state's-useful-information-details", response_model=UsefulInfoAboutStateSchema)
def update_states_useful_information_details(useful_info: UsefulInfoAboutStateSchemaIn):
    return UsefulInfoAboutStateController.update_states_useful_info_detail(info_title=useful_info.info_title,
                                                                           detail=useful_info.details,
                                                                           state_id=useful_info.state_id)


@world_destination_router.put("/update-state's-useful-information-about-visa",
                              response_model=UsefulInfoAboutStateSchema)
def update_states_useful_information_abot_visa(state_id: str, is_visa_needed: bool):
    return UsefulInfoAboutStateController.update_states_info_about_visa(is_visa_needed=is_visa_needed,
                                                                        state_id=state_id)


@world_destination_router.put("/update-state's-useful-information-about-vaccine",
                              response_model=UsefulInfoAboutStateSchema)
def update_states_useful_information_abot_vaccine(state_id: str, is_vaccine_needed: bool):
    return UsefulInfoAboutStateController.update_states_info_about_vaccine(is_vaccine_needed=is_vaccine_needed,
                                                                           state_id=state_id)


@world_destination_router.put("/update-state's-useful-information-about-insurance",
                              response_model=UsefulInfoAboutStateSchema)
def update_states_useful_information_abot_insurance(state_id: str, is_insurance_needed: bool):
    return UsefulInfoAboutStateController.update_states_info_about_insurance(is_insurance_needed=is_insurance_needed,
                                                                             state_id=state_id)


@world_destination_router.delete("/delete-state's-useful-information")
def delete_states_useful_information(state_id: str, info_title: str):
    return UsefulInfoAboutStateController.delete_states_useful_info(state_id=state_id, info_title=info_title)
