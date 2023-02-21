from sqlalchemy.exc import IntegrityError

from app.arrangements.exceptions import PlanAndProgramAlreadyExistsException, PlanAndProgramNotFoundException, ExcursionNotFoundException
from app.database.db import SessionLocal
from app.arrangements.repository import PlanAndProgramPerDayRepository, ExcursionRepository


class PlanAndProgramPerDayService:

    @staticmethod
    def create_plan_and_program_per_day(title: str, location: str, description: str, food: str, excursion_id: str,
                                        accommodation_id: str, arrangement_id: str):
        with SessionLocal() as db:
            try:
                plan_and_program_per_day_repository = PlanAndProgramPerDayRepository(db)
                return plan_and_program_per_day_repository.create_plan_and_program_per_day(title=title,
                                                                                           location=location,
                                                                                           description=description,
                                                                                           food=food,
                                                                                           excursion_id=excursion_id,
                                                                                           accommodation_id=accommodation_id,
                                                                                           arrangement_id=arrangement_id)
            except IntegrityError:
                raise PlanAndProgramAlreadyExistsException(code=400,
                                                           message="This plan and program already exists in database.")
            except Exception as e:
                raise e

    @staticmethod
    def get_all_plans_and_programs_for_arrangement(arrangement_id: str):
        with SessionLocal() as db:
            try:
                plan_and_program_per_day_repository = PlanAndProgramPerDayRepository(db)
                p_and_ps = plan_and_program_per_day_repository.get_all_plans_and_programs_for_arrangement(
                    arrangement_id=arrangement_id)
                if p_and_ps:
                    return p_and_ps
                raise PlanAndProgramNotFoundException(code=400,
                                                      message=f"Currently there are no plans and programs per day for arrangement with ID {arrangement_id}.")
            except Exception as e:
                raise e

    @staticmethod
    def get_all_excursions_for_arrangement(arrangement_id: str):
        with SessionLocal() as db:
            try:
                plan_and_program_per_day_repository = PlanAndProgramPerDayRepository(db)
                excursion_repository = ExcursionRepository(db)
                p_and_ps = plan_and_program_per_day_repository.get_all_plans_and_programs_for_arrangement(
                    arrangement_id=arrangement_id)
                if p_and_ps:
                    excursions = []
                    for p_and_p in p_and_ps:
                        if excursion_repository.get_excursion_by_id(excursion_id=p_and_p.excursion_id):
                            excursions.append(excursion_repository.get_excursion_by_id(excursion_id=p_and_p.excursion_id))
                        pass
                    if excursions:
                        return excursions
                    raise ExcursionNotFoundException(code=400, message="Currently, this arrangement does not have eny excursions.")
                raise PlanAndProgramNotFoundException(code=400,
                                                      message=f"Currently there are no plans and programs per day for arrangement with ID {arrangement_id}.")
            except Exception as e:
                raise e

    @staticmethod
    def get_all_excursions_for_arrangement_under_price(arrangement_id: str, price: float):
        with SessionLocal() as db:
            try:
                plan_and_program_per_day_repository = PlanAndProgramPerDayRepository(db)
                excursion_repository = ExcursionRepository(db)
                p_and_ps = plan_and_program_per_day_repository.get_all_plans_and_programs_for_arrangement(
                    arrangement_id=arrangement_id)
                if p_and_ps:
                    excursions = []
                    for p_and_p in p_and_ps:
                        if excursion_repository.get_excursion_by_id(excursion_id=p_and_p.excursion_id):
                            excursions.append(excursion_repository.get_excursion_by_id(excursion_id=p_and_p.excursion_id))
                        pass
                    if excursions:
                        if [excursion for excursion in excursions if excursion.price <= price]:
                            return [excursion for excursion in excursions if excursion.price <= price]
                        raise ExcursionNotFoundException(code=400, message=f"Currently, this arrangement does not have eny excursions under price {price}.")
                    raise ExcursionNotFoundException(code=400, message="Currently, this arrangement does not have eny excursions.")
                raise PlanAndProgramNotFoundException(code=400,
                                                      message=f"Currently there are no plans and programs per day for arrangement with ID {arrangement_id}.")
            except Exception as e:
                raise e


    @staticmethod
    def get_plan_and_program_for_day_for_arrangement(day_num: int, arrangement_id: str):
        with SessionLocal() as db:
            try:
                plan_and_program_per_day_repository = PlanAndProgramPerDayRepository(db)
                p_and_p = plan_and_program_per_day_repository.get_plan_and_program_for_day_for_arrangement(
                    day_num=day_num, arrangement_id=arrangement_id)
                if p_and_p:
                    return p_and_p
                raise PlanAndProgramNotFoundException(code=400,
                                                      message=f"Plan and program for this day for arrangement  with ID {arrangement_id} does not exist.")
            except ValueError as e:
                raise e
            except Exception as e:
                raise e

    @staticmethod
    def get_plan_and_program_by_id(p_and_p_id: str):
        with SessionLocal() as db:
            try:
                plan_and_program_per_day_repository = PlanAndProgramPerDayRepository(db)
                p_and_p = plan_and_program_per_day_repository.get_plan_and_program_by_id(p_and_p_id=p_and_p_id)
                if p_and_p:
                    return p_and_p
                raise PlanAndProgramNotFoundException(code=400,
                                                      message=f"Plan and program with provided ID {p_and_p_id} does not exist.")
            except Exception as e:
                raise e

    @staticmethod
    def update_plan_and_program_per_day(p_and_p_id: str, title: str, location: str, description: str, food: str,
                                        excursion_id: str,
                                        accommodation_id: str):
        with SessionLocal() as db:
            try:
                plan_and_program_per_day_repository = PlanAndProgramPerDayRepository(db)
                p_and_p = plan_and_program_per_day_repository.get_plan_and_program_by_id(p_and_p_id=p_and_p_id)
                if p_and_p:
                    return plan_and_program_per_day_repository.update_plan_and_program_per_day(p_and_p_id=p_and_p_id,
                                                                                               title=title,
                                                                                               location=location,
                                                                                               description=description,
                                                                                               food=food,
                                                                                               excursion_id=excursion_id,
                                                                                               accommodation_id=accommodation_id)
                raise PlanAndProgramNotFoundException(code=400,
                                                      message=f"Plan and program with provided ID {p_and_p_id} does not exist.")
            except Exception as e:
                raise e

    @staticmethod
    def delete_plan_and_program_per_day_by_id(p_and_p_id: str):
        with SessionLocal() as db:
            try:
                plan_and_program_per_day_repository = PlanAndProgramPerDayRepository(db)
                if plan_and_program_per_day_repository.delete_plan_and_program_per_day_by_id(p_and_p_id=p_and_p_id):
                    return True
                raise PlanAndProgramNotFoundException(code=400,
                                                      message=f"Plan and program with provided ID {p_and_p_id} does not exist.")
            except Exception as e:
                raise e
