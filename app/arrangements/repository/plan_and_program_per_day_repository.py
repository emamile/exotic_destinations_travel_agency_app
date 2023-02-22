from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.arrangements.models.plan_and_program_per_day import PlanAndProgramPerDay


# > This class is responsible for retrieving the plan and program for a given day
class PlanAndProgramPerDayRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_arrangements_plan_and_program_per_day(
        self, title: str, location: str, description: str, arrangement_id: str, food: str = None, excursion_id: str = None, accommodation_id: str = None
    ):
        """
        It creates a new PlanAndProgramPerDay object and adds it to the database

        :param title: str,
        :type title: str
        :param location: str,
        :type location: str
        :param description: str, food: str, excursion_id: str, accommodation_id: str, arrangement_id: str
        :type description: str
        :param food: str,
        :type food: str
        :param excursion_id: str,
        :type excursion_id: str
        :param accommodation_id: str, arrangement_id: str, excursion_id: str
        :type accommodation_id: str
        :param arrangement_id: The id of the arrangement that the plan and program per day belongs to
        :type arrangement_id: str
        :return: the created plan and program per day.
        """

        try:
            p_and_p = PlanAndProgramPerDay(
                title=title,
                location=location,
                description=description,
                food=food,
                excursion_id=excursion_id,
                accommodation_id=accommodation_id,
                arrangement_id=arrangement_id,
            )

            self.db.add(p_and_p)
            self.db.commit()
            self.db.refresh(p_and_p)
            return p_and_p
        except IntegrityError as e:
            raise e
        except ValueError as e:
            raise e

    def get_arrangements_plans_and_programs_per_day(self, arrangement_id: str):
        """
        It returns a list of all the plans and programs per day for a given arrangement

        :param arrangement_id: str
        :type arrangement_id: str
        :return: A list of PlanAndProgramPerDay objects
        """
        try:
            p_and_ps = self.db.query(PlanAndProgramPerDay).filter(PlanAndProgramPerDay.arrangement_id == arrangement_id).all()
            return p_and_ps
        except Exception as e:
            raise e

    def get_arrangements_plan_and_program_for_day(self, day_num: int, arrangement_id: str):
        """
        It takes in a day number and an arrangement id and returns the plan and program for that day

        :param day_num: int
        :type day_num: int
        :param arrangement_id: The id of the arrangement
        :type arrangement_id: str
        :return: A list of all the arrangements for a given user.
        """
        try:
            p_and_p = (
                self.db.query(PlanAndProgramPerDay)
                .filter(PlanAndProgramPerDay.arrangement_id == arrangement_id, PlanAndProgramPerDay.title.ilike(f"%{day_num}%"))
                .first()
            )
            return p_and_p
        except ValueError as e:
            raise e
        except Exception as e:
            raise e

    def get_arrangements_plan_and_program_by_id(self, p_and_p_id: str):
        """
        It gets the plan and program for a given day by id

        :param p_and_p_id: The id of the plan and program
        :type p_and_p_id: str
        :return: A list of all the arrangements for a specific plan and program per day.
        """
        try:
            p_and_p = self.db.query(PlanAndProgramPerDay).filter(PlanAndProgramPerDay.id == p_and_p_id).first()
            return p_and_p
        except Exception as e:
            raise e

    def update_arrangements_plan_and_program_per_day(
        self,
        p_and_p_id: str,
        title: str = None,
        location: str = None,
        description: str = None,
        food: str = None,
        excursion_id: str = None,
        accommodation_id: str = None,
    ):
        """
        It updates the plan and program per day with the given id with the given parameters

        :param p_and_p_id: str = The id of the plan and program per day you want to update
        :type p_and_p_id: str
        :param title: str = None,
        :type title: str
        :param location: str = None,
        :type location: str
        :param description: str = None,
        :type description: str
        :param food: str = None,
        :type food: str
        :param excursion_id: str = None,
        :type excursion_id: str
        :param accommodation_id: str = None,
        :type accommodation_id: str
        :return: A list of all the arrangements
        """

        try:
            p_and_p = self.db.query(PlanAndProgramPerDay).filter(PlanAndProgramPerDay.id == p_and_p_id).first()
            if title is not None:
                p_and_p.title = title
            if location is not None:
                p_and_p.location = location
            if description is not None:
                p_and_p.description = description
            if food is not None:
                p_and_p.food = food
            if excursion_id is not None:
                p_and_p.excursion_id = excursion_id
            if accommodation_id is not None:
                p_and_p.accommodation_id = accommodation_id
            self.db.add(p_and_p)
            self.db.commit()
            self.db.refresh(p_and_p)
            return p_and_p
        except Exception as e:
            raise e

    def delete_arrangements_plan_and_program_per_day_by_id(self, p_and_p_id: str):
        """
        It deletes a row from the database table "PlanAndProgramPerDay" where the id of the row is equal to the parameter
        "p_and_p_id"

        :param p_and_p_id: The id of the plan and program per day
        :type p_and_p_id: str
        :return: A list of all the arrangements, plans and programs per day.
        """
        try:
            p_and_p = self.db.query(PlanAndProgramPerDay).filter(PlanAndProgramPerDay.id == p_and_p_id).first()
            if p_and_p is None:
                return False
            self.db.delete(p_and_p)
            self.db.commit()
            return True
        except Exception as e:
            raise e
