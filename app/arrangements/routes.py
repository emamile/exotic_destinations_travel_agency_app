import typing as t

from fastapi import APIRouter, Depends

from app.arrangements.controller.accommodation_controller import AccommodationController
from app.arrangements.controller.arrangement_controller import ArrangementController
from app.arrangements.controller.excursion_controller import ExcursionController
from app.arrangements.controller.plan_and_program_per_day_controller import PlanAndProgramPerDayController
from app.arrangements.schemas.accommodation_schema import AccommodationSchema, AccommodationSchemaIn, AccommodationSchemaUpdate
from app.arrangements.schemas.arrangement_schema import ArrangementSchema, ArrangementSchemaIn, ArrangementSchemaUpdate
from app.arrangements.schemas.excursion_schema import ExcursionSchema, ExcursionSchemaIn, ExcursionSchemaUpdate
from app.arrangements.schemas.plan_and_program_per_day_schema import (
    PlanAndProgramPerDaySchema,
    PlanAndProgramPerDaySchemaIn,
    PlanAndProgramPerDaySchemaUpdate,
)
from app.users.controller.user_auth_handler_controller import JWTBearer
from app.users.schemas import BookedArrangementSchema

arrangement_router = APIRouter(tags=["ARRANGEMENTS"], prefix="/api/arrangements")
accommodation_router = APIRouter(tags=["ACCOMMODATIONS"], prefix="/api/accommodations")
excursion_router = APIRouter(tags=["EXCURSIONS"], prefix="/api/excursions")


@arrangement_router.post("/add-arrangement", response_model=ArrangementSchema, dependencies=[Depends(JWTBearer("superuser"))])
def add_arrangement(arrangement: ArrangementSchemaIn):
    """
    It creates an arrangement

    :param arrangement: ArrangementSchemaIn
    :type arrangement: ArrangementSchemaIn
    :return: Arrangement object
    """
    return ArrangementController.create_arrangement(
        name=arrangement.name,
        code=arrangement.code,
        date_of_departure=arrangement.date_of_departure,
        date_of_arrival=arrangement.date_of_arrival,
        duration=arrangement.duration,
        description=arrangement.description,
        air_route_to_the_destination=arrangement.air_route_to_the_destination,
        price=arrangement.price,
        demandingness=arrangement.demandingness,
        availability=arrangement.availability,
        included_in_price=arrangement.included_in_price,
        not_included_in_price=arrangement.not_included_in_price,
        state_id=arrangement.state_id,
    )


@arrangement_router.get("/get-all-arrangements-for-state", response_model=list[ArrangementSchema])
def get_all_arrangements_for_state(state_id: str):
    """
    > Get all arrangements for a given state

    :param state_id: The id of the state you want to get arrangements for
    :type state_id: str
    :return: A list of all arrangements for a given state.
    """
    return ArrangementController.get_all_arrangements_for_state(state_id=state_id)


@arrangement_router.get("/get-all-arrangements-for-world-destination")
def get_all_arrangements_for_world_destination(world_destination_id: str):
    """
    > Get all arrangements for a world destination

    :param world_destination_id: The id of the world destination you want to get all arrangements for
    :type world_destination_id: str
    :return: A list of all the arrangements for a given world destination.
    """
    return ArrangementController.get_all_arrangements_for_world_destination(world_destination_id=world_destination_id)


@arrangement_router.get("/get-arrangement-by-id", response_model=ArrangementSchema, dependencies=[Depends(JWTBearer("superuser"))])
def get_arrangement_by_id(arrangement_id: str):
    """
    `get_arrangement_by_id` returns an arrangement object given an arrangement id

    :param arrangement_id: The ID of the arrangement you want to get
    :type arrangement_id: str
    :return: A list of all the arrangements
    """
    return ArrangementController.get_arrangement_by_id(arrangement_id=arrangement_id)


@arrangement_router.get("/get-arrangement-by-code", response_model=ArrangementSchema, dependencies=[Depends(JWTBearer("superuser"))])
def get_arrangement_by_code(code: str):
    """
    `get_arrangement_by_code` returns an arrangement object given a code

    :param code: The code of the arrangement you want to get
    :type code: str
    :return: A list of Arrangement objects
    """
    return ArrangementController.get_arrangement_by_code(code=code)


@arrangement_router.get("/get-arrangement-under-price", response_model=list[ArrangementSchema])
def get_arrangements_under_price(price: float):
    """
    > This function returns all the arrangements that are under a certain price

    :param price: float
    :type price: float
    :return: A list of arrangements that are under the price given.
    """
    return ArrangementController.get_arrangement_under_price(price=price)


@arrangement_router.get(
    "/get-all-booked-arrangements", response_model=list[BookedArrangementSchema], dependencies=[Depends(JWTBearer("superuser"))]
)
def get_all_booked_arrangements():
    """
    It returns a list of all booked arrangements
    :return: A list of all booked arrangements.
    """
    return ArrangementController.get_all_booked_arrangements()


@arrangement_router.get("/get-all-booked-arrangement's-travelers", dependencies=[Depends(JWTBearer("superuser"))])
def get_all_booked_arrangements_travelers(arrangement_id: str):
    """
    Get all travelers that booked an arrangement

    :param arrangement_id: str
    :type arrangement_id: str
    :return: A list of all the travelers that have booked the arrangement.
    """
    return ArrangementController.get_all_booked_arrangement_travelers(arrangement_id=arrangement_id)


@arrangement_router.put(
    "/update-arrangements-price-and-availability", response_model=ArrangementSchema, dependencies=[Depends(JWTBearer("superuser"))]
)
def update_arrangements_price_and_availability(arrangement: ArrangementSchemaUpdate):
    """
    `update_arrangements_price_and_availability` updates the price and availability of an arrangement

    :param arrangement: ArrangementSchemaUpdate
    :type arrangement: ArrangementSchemaUpdate
    :return: The updated arrangement
    """
    return ArrangementController.update_arrangements_price_and_availability(
        arrangement_id=arrangement.id, price=arrangement.price, availability=arrangement.availability
    )


@arrangement_router.delete("/delete-arrangement-by-id", dependencies=[Depends(JWTBearer("superuser"))])
def delete_arrangement_by_id(arrangement_id: str):
    """
    Delete an arrangement by its id

    :param arrangement_id: The id of the arrangement you want to delete
    :type arrangement_id: str
    :return: The arrangement_id of the arrangement that was deleted.
    """
    return ArrangementController.delete_arrangement_by_id(arrangement_id=arrangement_id)


@arrangement_router.post(
    "/add-arrangement's-plan-and-program-for-day", response_model=PlanAndProgramPerDaySchema, dependencies=[Depends(JWTBearer("superuser"))]
)
def create_arrangements_plan_and_program_per_day(p_and_p: PlanAndProgramPerDaySchemaIn):
    """
    It creates a new plan and program per day for an arrangement

    :param p_and_p: PlanAndProgramPerDaySchemaIn
    :type p_and_p: PlanAndProgramPerDaySchemaIn
    :return: The created plan and program per day.
    """
    return PlanAndProgramPerDayController.create_arrangements_plan_and_program_per_day(
        title=p_and_p.title,
        location=p_and_p.location,
        description=p_and_p.description,
        food=p_and_p.food,
        excursion_id=p_and_p.excursion_id,
        accommodation_id=p_and_p.accommodation_id,
        arrangement_id=p_and_p.arrangement_id,
    )


@arrangement_router.get("/get-arrangement's-plans-and-programs-per-day", response_model=list[PlanAndProgramPerDaySchema])
def get_arrangements_plans_and_programs_per_day(arrangement_id: str):
    """
    > Get all plans and programs per day for a given arrangement

    :param arrangement_id: The arrangement id of the arrangement you want to get the plans and programs per day for
    :type arrangement_id: str
    :return: A list of dictionaries containing the plans and programs per day for a given arrangement.
    """
    return PlanAndProgramPerDayController.get_arrangements_plans_and_programs_per_day(arrangement_id=arrangement_id)


@arrangement_router.get("/get-arrangement's-plan-and-program-for-day", response_model=PlanAndProgramPerDaySchema)
def get_arrangements_plan_and_program_for_day(day_num: int, arrangement_id: str):
    """
    > Get the plan and program for a specific day of a specific arrangement

    :param day_num: The day number of the plan and program
    :type day_num: int
    :param arrangement_id: The id of the arrangement you want to get the plan and program for
    :type arrangement_id: str
    :return: A list of dictionaries, each dictionary contains the following keys:
        - day_num
        - arrangement_id
        - plan_and_program_id
        - plan_and_program_name
        - plan_and_program_description
        - plan_and_program_type
        - plan_and_program_start_time
        -
    """
    return PlanAndProgramPerDayController.get_arrangements_plan_and_program_for_day(day_num=day_num, arrangement_id=arrangement_id)


@arrangement_router.get("/get-arrangement's-excursions")
def get_arrangements_excursions(arrangement_id: str):
    """
    `get_arrangements_excursions` returns a list of excursions for a given arrangement

    :param arrangement_id: The id of the arrangement you want to get the excursions for
    :type arrangement_id: str
    :return: A list of excursions
    """
    return ArrangementController.get_arrangements_excursions(arrangement_id=arrangement_id)


@arrangement_router.get("/get-arrangement's-accommodations")
def get_arrangements_accommodations(arrangement_id: str):
    """
    Get the accommodations for a given arrangement

    :param arrangement_id: The arrangement ID of the arrangement you want to get the accommodations for
    :type arrangement_id: str
    :return: A list of accommodations for a given arrangement.
    """
    return ArrangementController.get_arrangements_accommodations(arrangement_id=arrangement_id)


@arrangement_router.get("/get-arrangement's-excursions-under-price")
def get_all_excursions_for_arrangement_under_price(arrangement_id: str, price: float):
    """
    > Get all excursions for arrangement under price

    :param arrangement_id: The id of the arrangement you want to get the excursions for
    :type arrangement_id: str
    :param price: float
    :type price: float
    :return: A list of excursions that are under a certain price.
    """
    return ArrangementController.get_arrangements_excursions_under_price(arrangement_id=arrangement_id, price=price)


@arrangement_router.get(
    "/get-arrangement's-plan-and-program-per-day-by-id",
    response_model=PlanAndProgramPerDaySchema,
    dependencies=[Depends(JWTBearer("superuser"))],
)
def get_arrangements_plan_and_program_by_id(p_and_p_id: str):
    """
    > This function returns a list of arrangements of a plan and program by its id

    :param p_and_p_id: The id of the plan and program
    :type p_and_p_id: str
    :return: A list of arrangements
    """
    return PlanAndProgramPerDayController.get_arrangements_plan_and_program_by_id(p_and_p_id=p_and_p_id)


@arrangement_router.put(
    "/update-arrangement's-plan-and-program-per-day",
    response_model=PlanAndProgramPerDaySchema,
    dependencies=[Depends(JWTBearer("superuser"))],
)
def update_arrangements_plan_and_program_per_day(p_and_p: PlanAndProgramPerDaySchemaUpdate):
    """
    `update_arrangements_plan_and_program_per_day` is a function that updates the arrangements of a plan and program per day

    :param p_and_p: PlanAndProgramPerDaySchemaUpdate
    :type p_and_p: PlanAndProgramPerDaySchemaUpdate
    :return: The updated plan and program per day.
    """
    return PlanAndProgramPerDayController.update_arrangements_plan_and_program_per_day(
        p_and_p_id=p_and_p.id,
        title=p_and_p.title,
        location=p_and_p.location,
        description=p_and_p.description,
        food=p_and_p.food,
        excursion_id=p_and_p.excursion_id,
        accommodation_id=p_and_p.accommodation_id,
    )


@arrangement_router.delete("/delete-arrangement's-plan-and-program-per-day-by-id", dependencies=[Depends(JWTBearer("superuser"))])
def delete_arrangements_plan_and_program_per_day_by_id(p_and_p_id: str):
    """
    Delete arrangements plan and program per day by id

    :param p_and_p_id: str
    :type p_and_p_id: str
    :return: A list of dictionaries.
    """
    return PlanAndProgramPerDayController.delete_arrangements_plan_and_program_per_day_by_id(p_and_p_id=p_and_p_id)


@accommodation_router.post("/add-accommodation", response_model=AccommodationSchema, dependencies=[Depends(JWTBearer("superuser"))])
def add_accommodation(accommodation: AccommodationSchemaIn):
    """
    `add_accommodation` takes an `AccommodationSchemaIn` object and returns an `AccommodationSchemaOut` object

    :param accommodation: AccommodationSchemaIn
    :type accommodation: AccommodationSchemaIn
    :return: The accommodation object
    """
    return AccommodationController.create_accommodation(
        name=accommodation.name, type=accommodation.type, description=accommodation.description
    )


@accommodation_router.get("/get-all-accommodations", response_model=list[AccommodationSchema])
def get_all_accommodations():
    """
    It returns all the accommodations in the database.
    :return: A list of all the accommodations in the database.
    """
    return AccommodationController.get_all_accommodations()


@accommodation_router.get("/get-accommodation-by-id", response_model=AccommodationSchema, dependencies=[Depends(JWTBearer("superuser"))])
def get_accommodation_by_id(accommodation_id: str):
    """
    `Get accommodation by id.`

    :param accommodation_id: The id of the accommodation you want to get
    :type accommodation_id: str
    :return: A list of Accommodation objects
    """
    return AccommodationController.get_accommodation_by_id(accommodation_id=accommodation_id)


@accommodation_router.get("/get-all-types-of-accommodations", response_model=t.List[str])
def get_all_types_of_accommodations():
    """
    *|CURSOR_MARCADOR|*
    :return: A list of all the types of accommodations
    """
    return AccommodationController.get_all_types_of_accommodations()


@accommodation_router.get("/get-accommodations-by-type", response_model=list[AccommodationSchema])
def get_accommodations_by_type(type: str):
    """
    `get_accommodations_by_type` returns a list of accommodations that match the given type

    :param type: str
    :type type: str
    :return: A list of accommodations
    """
    return AccommodationController.get_accommodations_by_type(type=type)


@accommodation_router.put(
    "/update-accommodation's-description", response_model=AccommodationSchema, dependencies=[Depends(JWTBearer("superuser"))]
)
def update_accommodations_description(accommodation: AccommodationSchemaUpdate):
    """
    `update_accommodations_description` updates the description of an accommodation

    :param accommodation: AccommodationSchemaUpdate
    :type accommodation: AccommodationSchemaUpdate
    :return: The accommodation description is being returned.
    """
    return AccommodationController.update_accommodation_description(
        accommodation_id=accommodation.id, description=accommodation.description
    )


@accommodation_router.delete("/delete-accommodation-by-id", dependencies=[Depends(JWTBearer("superuser"))])
def delete_accommodation_by_id(accommodation_id: str):
    """
    Delete an accommodation by its id

    :param accommodation_id: str
    :type accommodation_id: str
    :return: A boolean value
    """
    return AccommodationController.delete_accommodation_by_id(accommodation_id=accommodation_id)


@excursion_router.post("/add-excursion", response_model=ExcursionSchema, dependencies=[Depends(JWTBearer("superuser"))])
def add_excursion(excursion: ExcursionSchemaIn):
    """
    > This function creates an excursion

    :param excursion: ExcursionSchemaIn
    :type excursion: ExcursionSchemaIn
    :return: The excursion object
    """
    return ExcursionController.create_excursion(name=excursion.name, price=excursion.price, description=excursion.description)


@excursion_router.get("/get-all-excursions", response_model=list[ExcursionSchema])
def get_all_excursions():
    """
    > This function returns all the excursions in the database
    :return: A list of all the excursions in the database.
    """
    return ExcursionController.get_all_excursions()


@excursion_router.get("/get-excursion-by-id", response_model=ExcursionSchema, dependencies=[Depends(JWTBearer("superuser"))])
def get_excursion_by_id(excursion_id: str):
    """
    `Get an excursion by its id.`

    :param excursion_id: The id of the excursion you want to get
    :type excursion_id: str
    :return: A list of excursions
    """
    return ExcursionController.get_excursion_by_id(excursion_id=excursion_id)


@excursion_router.put(
    "/update-excursion's-price-and-description", response_model=ExcursionSchema, dependencies=[Depends(JWTBearer("superuser"))]
)
def update_excursions_price_and_description(excursion: ExcursionSchemaUpdate):
    """
    `update_excursions_price_and_description` updates the price and description of an excursion

    :param excursion: ExcursionSchemaUpdate
    :type excursion: ExcursionSchemaUpdate
    :return: The excursion object
    """
    return ExcursionController.update_excursion_price_and_description(
        excursion_id=excursion.id, price=excursion.price, description=excursion.description
    )


@excursion_router.delete("/delete-excursion-by-id", dependencies=[Depends(JWTBearer("superuser"))])
def delete_excursion_by_id(excursion_id: str):
    """
    Delete an excursion by id

    :param excursion_id: str
    :type excursion_id: str
    :return: The excursion object that was deleted.
    """
    return ExcursionController.delete_excursion_by_id(excursion_id=excursion_id)
