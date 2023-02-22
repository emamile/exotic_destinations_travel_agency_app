from sqlalchemy.exc import IntegrityError

from app.arrangements.exceptions import (
    AccommodationNotFoundException,
    ExcursionNotFoundException,
    PlanAndProgramAlreadyExistsException,
    PlanAndProgramNotFoundException,
)
from app.arrangements.repository import AccommodationRepository, ExcursionRepository, PlanAndProgramPerDayRepository
from app.database.db import SessionLocal


# > This class is responsible for retrieving the plan and program for a given day
class PlanAndProgramPerDayService:
    @staticmethod
    def create_arrangements_plan_and_program_per_day(
        title: str, location: str, description: str, arrangement_id: str, food: str = None, excursion_id: str = None, accommodation_id: str = None
    ):
        """
        It creates a new plan and program per day for an arrangement

        :param title: str, location: str, description: str, food: str, excursion_id: str, accommodation_id: str,
        arrangement_id: str
        :type title: str
        :param location: str,
        :type location: str
        :param description: str, food: str, excursion_id: str, accommodation_id: str, arrangement_id: str
        :type description: str
        :param food: str, excursion_id: str, accommodation_id: str, arrangement_id: str
        :type food: str
        :param excursion_id: str,
        :type excursion_id: str
        :param accommodation_id: str, arrangement_id: str, excursion_id: str
        :type accommodation_id: str
        :param arrangement_id: str
        :type arrangement_id: str
        :return: the created plan and program per day.
        """

        try:
            with SessionLocal() as db:
                plan_and_program_per_day_repository = PlanAndProgramPerDayRepository(db)
                return plan_and_program_per_day_repository.create_arrangements_plan_and_program_per_day(
                    title=title,
                    location=location,
                    description=description,
                    food=food,
                    excursion_id=excursion_id,
                    accommodation_id=accommodation_id,
                    arrangement_id=arrangement_id,
                )
        except IntegrityError as exc:
            raise PlanAndProgramAlreadyExistsException(code=409, message="This plan and program already exists in database.") from exc
        except Exception as e:
            raise e

    @staticmethod
    def get_arrangements_plans_and_programs_per_day(arrangement_id: str):
        """
        It gets all the plans and programs per day for a given arrangement

        :param arrangement_id: str
        :type arrangement_id: str
        :return: A list of plans and programs per day for a specific arrangement.
        """
        try:
            with SessionLocal() as db:
                plan_and_program_per_day_repository = PlanAndProgramPerDayRepository(db)
                p_and_ps = plan_and_program_per_day_repository.get_arrangements_plans_and_programs_per_day(arrangement_id=arrangement_id)
                if p_and_ps:
                    return p_and_ps
                raise PlanAndProgramNotFoundException(
                    code=400, message=f"Currently there are no plans and programs per day for arrangement with ID {arrangement_id}."
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_all_excursions_for_arrangement(arrangement_id: str):
        """
        It gets all the excursions for a given arrangement

        :param arrangement_id: str
        :type arrangement_id: str
        :return: A list of excursions.
        """
        try:
            with SessionLocal() as db:
                plan_and_program_per_day_repository = PlanAndProgramPerDayRepository(db)
                excursion_repository = ExcursionRepository(db)
                p_and_ps = plan_and_program_per_day_repository.get_arrangements_plans_and_programs_per_day(arrangement_id=arrangement_id)
                if p_and_ps:
                    excursions = []
                    for p_and_p in p_and_ps:
                        if excursion_repository.get_excursion_by_id(excursion_id=p_and_p.excursion_id):
                            excursions.append(excursion_repository.get_excursion_by_id(excursion_id=p_and_p.excursion_id))
                        pass
                    if excursions:
                        return excursions
                    raise ExcursionNotFoundException(code=400, message="Currently, this arrangement does not have eny excursions.")
                raise PlanAndProgramNotFoundException(
                    code=400, message=f"Currently there are no plans and programs per day for arrangement with ID {arrangement_id}."
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_all_accommodations_for_arrangement(arrangement_id: str):
        """
        It gets all accommodations for a given arrangement

        :param arrangement_id: str
        :type arrangement_id: str
        :return: A list of accommodations.
        """
        try:
            with SessionLocal() as db:
                plan_and_program_per_day_repository = PlanAndProgramPerDayRepository(db)
                accommodation_repository = AccommodationRepository(db)
                p_and_ps = plan_and_program_per_day_repository.get_arrangements_plans_and_programs_per_day(arrangement_id=arrangement_id)
                if p_and_ps:
                    accommodations = []
                    for p_and_p in p_and_ps:
                        if accommodation_repository.get_accommodation_by_id(accommodation_id=p_and_p.accommodation_id):
                            accommodations.append(
                                accommodation_repository.get_accommodation_by_id(accommodation_id=p_and_p.accommodation_id)
                            )
                        pass
                    if accommodations:
                        return accommodations
                    raise AccommodationNotFoundException(code=400, message="Currently, this arrangement does not have eny accommodations.")
                raise PlanAndProgramNotFoundException(
                    code=400, message=f"Currently there are no plans and programs per day for arrangement with ID {arrangement_id}."
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_all_excursions_for_arrangement_under_price(arrangement_id: str, price: float):
        """
        It returns all excursions for a given arrangement that are under a given price

        :param arrangement_id: str
        :type arrangement_id: str
        :param price: float
        :type price: float
        :return: A list of excursions that are under the price.
        """
        try:
            with SessionLocal() as db:
                plan_and_program_per_day_repository = PlanAndProgramPerDayRepository(db)
                excursion_repository = ExcursionRepository(db)
                p_and_ps = plan_and_program_per_day_repository.get_arrangements_plans_and_programs_per_day(arrangement_id=arrangement_id)
                if p_and_ps:
                    excursions = []
                    for p_and_p in p_and_ps:
                        if excursion_repository.get_excursion_by_id(excursion_id=p_and_p.excursion_id):
                            excursions.append(excursion_repository.get_excursion_by_id(excursion_id=p_and_p.excursion_id))
                        pass
                    if excursions:
                        if [excursion for excursion in excursions if excursion.price <= price]:
                            return [excursion for excursion in excursions if excursion.price <= price]
                        raise ExcursionNotFoundException(
                            code=400, message=f"Currently, this arrangement does not have eny excursions under price {price}."
                        )
                    raise ExcursionNotFoundException(code=400, message="Currently, this arrangement does not have eny excursions.")
                raise PlanAndProgramNotFoundException(
                    code=400, message=f"Currently there are no plans and programs per day for arrangement with ID {arrangement_id}."
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_arrangements_plan_and_program_for_day(day_num: int, arrangement_id: str):
        """
        It gets the plan and program for a specific day for a specific arrangement

        :param day_num: int
        :type day_num: int
        :param arrangement_id: The ID of the arrangement
        :type arrangement_id: str
        :return: A list of PlanAndProgramPerDay objects
        """
        try:
            with SessionLocal() as db:
                plan_and_program_per_day_repository = PlanAndProgramPerDayRepository(db)
                p_and_p = plan_and_program_per_day_repository.get_arrangements_plan_and_program_for_day(
                    day_num=day_num, arrangement_id=arrangement_id
                )
                if p_and_p:
                    return p_and_p
                raise PlanAndProgramNotFoundException(
                    code=400, message=f"Plan and program for this day for arrangement  with ID {arrangement_id} does not exist."
                )
        except ValueError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def get_arrangements_plan_and_program_by_id(p_and_p_id: str):
        """
        It gets the plan and program per day by id

        :param p_and_p_id: str
        :type p_and_p_id: str
        :return: A list of all the arrangements for a plan and program
        """
        try:
            with SessionLocal() as db:
                plan_and_program_per_day_repository = PlanAndProgramPerDayRepository(db)
                p_and_p = plan_and_program_per_day_repository.get_arrangements_plan_and_program_by_id(p_and_p_id=p_and_p_id)
                if p_and_p:
                    return p_and_p
                raise PlanAndProgramNotFoundException(code=400, message=f"Plan and program with provided ID {p_and_p_id} does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def update_arrangements_plan_and_program_per_day(
        p_and_p_id: str, title: str, location: str, description: str, food: str, excursion_id: str, accommodation_id: str
    ):
        """
        It updates the plan and program per day with the given id

        :param p_and_p_id: str,
        :type p_and_p_id: str
        :param title: str, location: str, description: str, food: str, excursion_id: str, accommodation_id: str
        :type title: str
        :param location: str,
        :type location: str
        :param description: str, food: str, excursion_id: str, accommodation_id: str
        :type description: str
        :param food: str,
        :type food: str
        :param excursion_id: str,
        :type excursion_id: str
        :param accommodation_id: str,
        :type accommodation_id: str
        :return: The updated plan and program per day.
        """

        try:
            with SessionLocal() as db:
                plan_and_program_per_day_repository = PlanAndProgramPerDayRepository(db)

                return plan_and_program_per_day_repository.update_arrangements_plan_and_program_per_day(
                    p_and_p_id=p_and_p_id,
                    title=title,
                    location=location,
                    description=description,
                    food=food,
                    excursion_id=excursion_id,
                    accommodation_id=accommodation_id,
                )
        except Exception as e:
            raise e

    @staticmethod
    def delete_arrangements_plan_and_program_per_day_by_id(p_and_p_id: str):
        """
        It deletes a plan and program per day by id

        :param p_and_p_id: str
        :type p_and_p_id: str
        :return: A list of all the arrangements of the plan and program per day.
        """
        try:
            with SessionLocal() as db:
                plan_and_program_per_day_repository = PlanAndProgramPerDayRepository(db)
                if plan_and_program_per_day_repository.delete_arrangements_plan_and_program_per_day_by_id(p_and_p_id=p_and_p_id):
                    return True
                raise PlanAndProgramNotFoundException(code=400, message=f"Plan and program with provided ID {p_and_p_id} does not exist.")
        except Exception as e:
            raise e
