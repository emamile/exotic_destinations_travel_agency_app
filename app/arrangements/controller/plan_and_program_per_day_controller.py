from fastapi import HTTPException, Response
from app.arrangements.services.plan_and_program_per_day_service import PlanAndProgramPerDayService
from app.arrangements.services import ArrangementService, AccommodationService, ExcursionService
from app.arrangements.exceptions.exceptions import ArrangementNotFoundException, PlanAndProgramNotFoundException,\
    PlanAndProgramAlreadyExistsException, ExcursionNotFoundException, AccommodationNotFoundException


class PlanAndProgramPerDayController:

    @staticmethod
    def create_plan_and_program_per_day(title: str, location: str, description: str, food: str, excursion_id: str,
                                        accommodation_id: str, arrangement_id: str):
        try:
            if excursion_id:
                excursion = ExcursionService.get_excursion_by_id(excursion_id=excursion_id)
            if accommodation_id:
                accommodation = AccommodationService.get_accommodation_by_id(accommodation_id=accommodation_id)
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            p_and_p = PlanAndProgramPerDayService.create_plan_and_program_per_day(title=title,
                                                                                  location=location,
                                                                                  description=description,
                                                                                  food=food,
                                                                                  excursion_id=excursion_id,
                                                                                  accommodation_id=accommodation_id,
                                                                                  arrangement_id=arrangement_id)
            return p_and_p
        except ExcursionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except AccommodationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except PlanAndProgramAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_plans_and_programs_for_arrangement(arrangement_id: str):
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            p_and_ps = PlanAndProgramPerDayService.get_all_plans_and_programs_for_arrangement(arrangement_id=arrangement_id)
            return p_and_ps
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except PlanAndProgramNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_excursions_for_arrangement(arrangement_id: str):
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            excursions = PlanAndProgramPerDayService.get_all_excursions_for_arrangement(arrangement_id=arrangement_id)
            return excursions
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except PlanAndProgramNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ExcursionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_excursions_for_arrangement_under_price(arrangement_id: str, price: float):
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            excursions = PlanAndProgramPerDayService.get_all_excursions_for_arrangement_under_price(arrangement_id=arrangement_id, price=price)
            return excursions
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except PlanAndProgramNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ExcursionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_plan_and_program_for_day_for_arrangement(day_num: int, arrangement_id: str):
        try:
            arrangement = ArrangementService.get_arrangement_by_id(arrangement_id=arrangement_id)
            p_and_p = PlanAndProgramPerDayService.get_plan_and_program_for_day_for_arrangement(day_num=day_num, arrangement_id=arrangement_id)
            return p_and_p
        except ArrangementNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except PlanAndProgramNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid day number input. Input must be positive number below {arrangement.duration}.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_plan_and_program_by_id(p_and_p_id: str):
        try:
            p_and_p = PlanAndProgramPerDayService.get_plan_and_program_by_id(p_and_p_id=p_and_p_id)
            return p_and_p
        except PlanAndProgramNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_plan_and_program_per_day(p_and_p_id: str, title: str, location: str, description: str, food: str,
                                        excursion_id: str,
                                        accommodation_id: str):
        try:
            if excursion_id:
                excursion = ExcursionService.get_excursion_by_id(excursion_id=excursion_id)
            if accommodation_id:
                accommodation = AccommodationService.get_accommodation_by_id(accommodation_id=accommodation_id)
            p_and_p = PlanAndProgramPerDayService.update_plan_and_program_per_day(p_and_p_id=p_and_p_id, title=title, location=location,
                                                                                  description=description, food=food, excursion_id=excursion_id,
                                                                                  accommodation_id=accommodation_id)
            return p_and_p
        except ExcursionNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except AccommodationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except PlanAndProgramNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_plan_and_program_per_day_by_id(p_and_p_id: str):
        try:
            if PlanAndProgramPerDayService.delete_plan_and_program_per_day_by_id(p_and_p_id=p_and_p_id):
                return Response(status_code=200, content=f"Plan and program per day with ID {p_and_p_id} is deleted.")
        except PlanAndProgramNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
