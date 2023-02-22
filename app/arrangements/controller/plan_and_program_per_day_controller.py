from fastapi import HTTPException, Response

from app.arrangements.exceptions.exceptions import (
    AccommodationNotFoundException,
    ArrangementNotFoundException,
    ExcursionNotFoundException,
    PlanAndProgramAlreadyExistsException,
    PlanAndProgramNotFoundException,
)
from app.arrangements.services import AccommodationService, ArrangementService, ExcursionService
from app.arrangements.services.plan_and_program_per_day_service import PlanAndProgramPerDayService


# > This class is used to get the plan and program per day
class PlanAndProgramPerDayController:
    @staticmethod
    def create_arrangements_plan_and_program_per_day(
        title: str, location: str, description: str, food: str, excursion_id: str, accommodation_id: str, arrangement_id: str
    ):
        """
        It creates a plan and program per day for an arrangement

        :param title: str, location: str, description: str, food: str, excursion_id: str, accommodation_id: str,
        arrangement_id: str
        :type title: str
        :param location: str,
        :type location: str
        :param description: str, food: str, excursion_id: str, accommodation_id: str, arrangement_id: str
        :type description: str
        :param food: str,
        :type food: str
        :param excursion_id: str, accommodation_id: str, arrangement_id: str
        :type excursion_id: str
        :param accommodation_id: str, arrangement_id: str, excursion_id: str,
        :type accommodation_id: str
        :param arrangement_id: str,
        :type arrangement_id: str
        :return: The plan and program per day is being returned.
        """

        try:
            if excursion_id:
                excursion = ExcursionService.get_excursion_by_id(excursion_id=excursion_id)
            if accommodation_id:
                accommodation = AccommodationService.get_accommodation_by_id(accommodation_id=accommodation_id)
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            p_and_p = PlanAndProgramPerDayService.create_arrangements_plan_and_program_per_day(
                title=title,
                location=location,
                description=description,
                food=food,
                excursion_id=excursion_id,
                accommodation_id=accommodation_id,
                arrangement_id=arrangement_id,
            )
            return p_and_p
        except ExcursionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except AccommodationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except PlanAndProgramAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_arrangements_plans_and_programs_per_day(arrangement_id: str):
        """
        It gets the arrangement by id, then gets the plans and programs per day for that arrangement

        :param arrangement_id: str
        :type arrangement_id: str
        :return: A list of plans and programs per day
        """
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            p_and_ps = PlanAndProgramPerDayService.get_arrangements_plans_and_programs_per_day(arrangement_id=arrangement_id)
            return p_and_ps
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except PlanAndProgramNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_arrangements_plan_and_program_for_day(day_num: int, arrangement_id: str):
        """
        It gets the plan and program for a specific day of a specific arrangement

        :param day_num: int - the day number of the plan and program you want to get
        :type day_num: int
        :param arrangement_id: The id of the arrangement that the plan and program belongs to
        :type arrangement_id: str
        :return: A list of PlanAndProgramPerDay objects.
        """
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            p_and_p = PlanAndProgramPerDayService.get_arrangements_plan_and_program_for_day(day_num=day_num, arrangement_id=arrangement_id)
            return p_and_p
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except PlanAndProgramNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except ValueError:
            raise HTTPException(
                status_code=400, detail=f"Invalid day number input. Input must be positive number below {arrangement.duration}."
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_arrangements_plan_and_program_by_id(p_and_p_id: str):
        """
        It gets the plan and program by id

        :param p_and_p_id: str
        :type p_and_p_id: str
        :return: A list of arrangements plan and program
        """
        try:
            p_and_p = PlanAndProgramPerDayService.get_arrangements_plan_and_program_by_id(p_and_p_id=p_and_p_id)
            return p_and_p
        except PlanAndProgramNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def update_arrangements_plan_and_program_per_day(
        p_and_p_id: str, title: str, location: str, description: str, food: str, excursion_id: str, accommodation_id: str
    ):
        """
        It updates the plan and program per day with the given id

        :param p_and_p_id: str, title: str, location: str, description: str, food: str, excursion_id: str, accommodation_id:
        str
        :type p_and_p_id: str
        :param title: str,
        :type title: str
        :param location: str,
        :type location: str
        :param description: str,
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
            if excursion_id:
                excursion = ExcursionService.get_excursion_by_id(excursion_id=excursion_id)
            if accommodation_id:
                accommodation = AccommodationService.get_accommodation_by_id(accommodation_id=accommodation_id)
            p_and_p = PlanAndProgramPerDayService.get_arrangements_plan_and_program_by_id(p_and_p_id=p_and_p_id)
            p_and_p = PlanAndProgramPerDayService.update_arrangements_plan_and_program_per_day(
                p_and_p_id=p_and_p_id,
                title=title,
                location=location,
                description=description,
                food=food,
                excursion_id=excursion_id,
                accommodation_id=accommodation_id,
            )
            return p_and_p
        except ExcursionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except AccommodationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except PlanAndProgramNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_arrangements_plan_and_program_per_day_by_id(p_and_p_id: str):
        """
        It deletes a plan and program per day by ID

        :param p_and_p_id: str
        :type p_and_p_id: str
        :return: A list of all the arrangements of the plan and program per day with the given ID.
        """
        try:
            if PlanAndProgramPerDayService.delete_arrangements_plan_and_program_per_day_by_id(p_and_p_id=p_and_p_id):
                return Response(status_code=200, content=f"Plan and program per day with ID {p_and_p_id} is deleted.")
        except PlanAndProgramNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
