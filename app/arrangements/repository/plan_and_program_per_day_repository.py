from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.arrangements.models.plan_and_program_per_day import PlanAndProgramPerDay


class PlanAndProgramPerDayRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_plan_and_program_per_day(self, title: str, location: str, description: str, food: str, excursion_id: str,
                                        accommodation_id: str, arrangement_id: str):
        try:
            p_and_p = PlanAndProgramPerDay(title=title, location=location, description=description, food=food,
                                           excursion_id=excursion_id, accommodation_id=accommodation_id,
                                           arrangement_id=arrangement_id)

            self.db.add(p_and_p)
            self.db.commit()
            self.db.refresh(p_and_p)
            return p_and_p
        except IntegrityError as e:
            raise e
        except ValueError as e:
            raise e

    def get_all_plans_and_programs_for_arrangement(self, arrangement_id: str):
        try:
            p_and_ps = self.db.query(PlanAndProgramPerDay).filter(
                PlanAndProgramPerDay.arrangement_id == arrangement_id).all()
            return p_and_ps
        except Exception as e:
            raise e

    def get_plan_and_program_for_day_for_arrangement(self, day_num: int, arrangement_id: str):
        try:
            p_and_p = self.db.query(PlanAndProgramPerDay).filter(
                PlanAndProgramPerDay.arrangement_id == arrangement_id, PlanAndProgramPerDay.title.ilike(
                    f"%{day_num}%")).first()
            return p_and_p
        except ValueError as e:
            raise e
        except Exception as e:
            raise e

    def get_plan_and_program_by_id(self, p_and_p_id: str):
        try:
            p_and_p = self.db.query(PlanAndProgramPerDay).filter(PlanAndProgramPerDay.id == p_and_p_id).first()
            return p_and_p
        except Exception as e:
            raise e

    def update_plan_and_program_per_day(self, p_and_p_id: str, title: str, location: str, description: str, food: str,
                                        excursion_id: str,
                                        accommodation_id: str):
        try:
            p_and_p = self.db.query(PlanAndProgramPerDay).filter(PlanAndProgramPerDay.id == p_and_p_id).first()
            p_and_p.title = title
            p_and_p.location = location
            p_and_p.description = description
            p_and_p.food = food
            p_and_p.excursion_id = excursion_id
            p_and_p.accommodation_id = accommodation_id
            self.db.add(p_and_p)
            self.db.commit()
            self.db.refresh(p_and_p)
            return p_and_p
        except Exception as e:
            raise e

    def delete_plan_and_program_per_day_by_id(self, p_and_p_id: str):
        try:
            p_and_p = self.db.query(PlanAndProgramPerDay).filter(PlanAndProgramPerDay.id == p_and_p_id).first()
            if p_and_p is None:
                return False
            self.db.delete(p_and_p)
            self.db.commit()
            return True
        except Exception as e:
            raise e
