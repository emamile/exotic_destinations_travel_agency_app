import json

from fastapi import APIRouter

from app.arrangements.controller.arrangement_controller import ArrangementController
from app.arrangements.controller.accommodation_controller import AccommodationController
from app.arrangements.controller.excursion_controller import ExcursionController
from app.arrangements.controller.plan_and_program_per_day_controller import PlanAndProgramPerDayController
from app.arrangements.schemas.arrangement_schema import ArrangementSchema, ArrangementSchemaIn, ArrangementSchemaUpdate
from app.arrangements.schemas.accommodation_schema import AccommodationSchema, AccommodationSchemaIn, \
    AccommodationSchemaUpdate
from app.arrangements.schemas.excursion_schema import ExcursionSchema, ExcursionSchemaIn, ExcursionSchemaUpdate
from app.arrangements.schemas.plan_and_program_per_day_schema import PlanAndProgramPerDaySchema, \
    PlanAndProgramPerDaySchemaIn, PlanAndProgramPerDaySchemaUpdate
import typing as t

arrangement_router = APIRouter(tags=["ARRANGEMENTS"], prefix="/api/arrangements")


@arrangement_router.post("/add-arrangement", response_model=ArrangementSchema)
def add_arrangement(arrangement: ArrangementSchemaIn):
    return ArrangementController.create_arrangement(name=arrangement.name, code=arrangement.code,
                                                    date_of_departure=arrangement.date_of_departure,
                                                    date_of_arrival=arrangement.date_of_arrival,
                                                    duration=arrangement.duration, description=arrangement.description,
                                                    air_route_to_the_destination=arrangement.air_route_to_the_destination,
                                                    price=arrangement.price, demandingness=arrangement.demandingness,
                                                    availability=arrangement.availability,
                                                    included_in_price=arrangement.included_in_price,
                                                    not_included_in_price=arrangement.not_included_in_price,
                                                    state_id=arrangement.state_id
                                                    )


@arrangement_router.get("/get-all-arrangements-for-state", response_model=list[ArrangementSchema])
def get_all_arrangements_for_state(state_id: str):
    return ArrangementController.get_all_arrangements_for_state(state_id=state_id)


@arrangement_router.get("/get-all-arrangements-for-world-destination")
def get_all_arrangements_for_world_destination(world_destination_id: str):
    return ArrangementController.get_all_arrangements_for_world_destination(world_destination_id=world_destination_id)


@arrangement_router.get("/get-arrangement-by-id", response_model=ArrangementSchema)
def get_arrangement_by_id(arrangement_id: str):
    return ArrangementController.get_arrangement_by_id(arrangement_id=arrangement_id)


@arrangement_router.get("/get-arrangement-by-code", response_model=ArrangementSchema)
def get_arrangement_by_code(code: str):
    return ArrangementController.get_arrangement_by_code(code=code)


@arrangement_router.get("/get-arrangement-under-price", response_model=list[ArrangementSchema])
def get_arrangements_under_price(price: float):
    return ArrangementController.get_arrangement_under_price(price=price)


@arrangement_router.get("/get-all-booked-arrangements", response_model=list[ArrangementSchema])
def get_all_booked_arrangements():
    return ArrangementController.get_all_booked_arrangements()


@arrangement_router.get("/get-all-booked-arrangement's-travelers", response_model=t.List[json])
def get_all_booked_arrangements_travelers(arrangement_id: str):
    return ArrangementController.get_all_booked_arrangement_travelers(arrangement_id=arrangement_id)


@arrangement_router.put("/update-arrangements-price-and-availability", response_model=ArrangementSchema)
def update_arrangements_price_and_availability(arrangement: ArrangementSchemaUpdate):
    return ArrangementController.update_arrangements_price_and_availability(arrangement_id=arrangement.id,
                                                                            price=arrangement.price,
                                                                            availability=arrangement.availability)


@arrangement_router.delete("/delete-arrangement-by-id")
def delete_arrangement_by_id(arrangement_id: str):
    return ArrangementController.delete_arrangement_by_id(arrangement_id=arrangement_id)


@arrangement_router.post("/add-accommodation", response_model=AccommodationSchema)
def add_accommodation(accommodation: AccommodationSchemaIn):
    return AccommodationController.create_accommodation(name=accommodation.name,
                                                        accommodation_type=accommodation.accommodation_type,
                                                        description=accommodation.description)


@arrangement_router.get("/get-all-accommodations", response_model=list[AccommodationSchema])
def get_all_accommodations():
    return AccommodationController.get_all_accommodations()


@arrangement_router.get("/get-accommodation-by-id", response_model=AccommodationSchema)
def get_accommodation_by_id(accommodation_id: str):
    return AccommodationController.get_accommodation_by_id(accommodation_id=accommodation_id)


@arrangement_router.get("/get-all-types-of-accommodations", response_model=t.List[str])
def get_all_types_of_accommodations():
    return AccommodationController.get_all_types_of_accommodations()


@arrangement_router.get("/get-accommodation-by-type", response_model=list[AccommodationSchema])
def get_accommodation_by_type(type: str):
    return AccommodationController.get_accommodations_by_type(type=type)


@arrangement_router.put("/update-accommodation-description", response_model=AccommodationSchema)
def update_accommodation_description(accommodation: AccommodationSchemaUpdate):
    return AccommodationController.update_accommodation_description(accommodation_id=accommodation.id,
                                                                    description=accommodation.description)


@arrangement_router.delete("/delete-accommodation-by-id")
def delete_accommodation_by_id(accommodation_id: str):
    return AccommodationController.delete_accommodation_by_id(accommodation_id=accommodation_id)


@arrangement_router.post("/add-excursion", response_model=ExcursionSchema)
def add_excursion(excursion: ExcursionSchemaIn):
    return ExcursionController.create_excursion(name=excursion.name, price=excursion.price,
                                                description=excursion.description)


@arrangement_router.get("/get-all-excursions", response_model=list[ExcursionSchema])
def get_all_excursions():
    return ExcursionController.get_all_excursions()


@arrangement_router.get("/get-excursion-by-id", response_model=ExcursionSchema)
def get_excursion_by_id(excursion_id: str):
    return ExcursionController.get_excursion_by_id(excursion_id=excursion_id)


@arrangement_router.put("/update-excursion-price-and-description", response_model=ExcursionSchema)
def update_excursion_price_and_description(excursion: ExcursionSchemaUpdate):
    return ExcursionController.update_excursion_price_and_description(excursion_id=excursion.id, price=excursion.price,
                                                                      description=excursion.description)


@arrangement_router.delete("/delete-excursion-by-id")
def delete_excursion_by_id(excursion_id: str):
    return ExcursionController.delete_excursion_by_id(excursion_id=excursion_id)


@arrangement_router.post("/add-plan-and-program-per-day-for-arrangement", response_model=PlanAndProgramPerDaySchema)
def add_plan_and_program_per_day_for_arrangement(p_and_p: PlanAndProgramPerDaySchemaIn):
    return PlanAndProgramPerDayController.create_plan_and_program_per_day(title=p_and_p.title,
                                                                          location=p_and_p.location,
                                                                          description=p_and_p.description,
                                                                          food=p_and_p.food,
                                                                          excursion_id=p_and_p.excursion_id,
                                                                          accommodation_id=p_and_p.accommodation_id,
                                                                          arrangement_id=p_and_p.arrangement_id)


@arrangement_router.get("/get-all-plans-and-programs-per-day-for-arrangement",
                        response_model=list[PlanAndProgramPerDaySchema])
def get_all_plans_and_programs_for_arrangement(arrangement_id: str):
    return PlanAndProgramPerDayController.get_all_plans_and_programs_for_arrangement(arrangement_id=arrangement_id)


@arrangement_router.get("/get-plan-and-program-for-day-for-arrangement", response_model=PlanAndProgramPerDaySchema)
def get_plan_and_program_for_day_for_arrangement(day_num: int, arrangement_id: str):
    return PlanAndProgramPerDayController.get_plan_and_program_for_day_for_arrangement(day_num=day_num,
                                                                                       arrangement_id=arrangement_id)


@arrangement_router.get("/get-all-excursions-for-arrangement")
def get_all_excursions_for_arrangement(arrangement_id: str):
    return PlanAndProgramPerDayController.get_all_excursions_for_arrangement(arrangement_id=arrangement_id)


@arrangement_router.get("/get-all-excursions-for-arrangement-under-price")
def get_all_excursions_for_arrangement_under_price(arrangement_id: str, price: float):
    return PlanAndProgramPerDayController.get_all_excursions_for_arrangement_under_price(arrangement_id=arrangement_id, price=price)


@arrangement_router.get("/get-plan-and-program-per-day-by-id", response_model=PlanAndProgramPerDaySchema)
def get_plan_and_program_by_id(p_and_p_id: str):
    return PlanAndProgramPerDayController.get_plan_and_program_by_id(p_and_p_id=p_and_p_id)


@arrangement_router.put("/update-plan-and-program-per-day", response_model=PlanAndProgramPerDaySchema)
def update_plan_and_program_per_day(p_and_p: PlanAndProgramPerDaySchemaUpdate):
    return PlanAndProgramPerDayController.update_plan_and_program_per_day(p_and_p_id=p_and_p.id, title=p_and_p.title,
                                                                          location=p_and_p.location,
                                                                          description=p_and_p.description,
                                                                          food=p_and_p.food,
                                                                          excursion_id=p_and_p.excursion_id,
                                                                          accommodation_id=p_and_p.accommodation_id)


@arrangement_router.delete("/delete-plan-and-program-per-day-by-id")
def delete_plan_and_program_per_day_by_id(p_and_p_id: str):
    return PlanAndProgramPerDayController.delete_plan_and_program_per_day_by_id(p_and_p_id=p_and_p_id)
