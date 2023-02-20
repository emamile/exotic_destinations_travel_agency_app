from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from datetime import date, datetime
from app.arrangements.models.arrangement import Arrangement


class ArrangementRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_arrangement(self, name: str, code: str, date_of_departure: str, date_of_arrival: str,
                           duration: int, description: str, air_route_to_the_destination: str,
                           price: float, demandingness: int, availability: bool, included_in_price: str,
                           not_included_in_price: str, state_id: str):
        try:
            arrangement = Arrangement(name=name, code=code, date_of_departure=date_of_departure,
                                      date_of_arrival=date_of_arrival,
                                      duration=duration, description=description,
                                      air_route_to_the_destination=air_route_to_the_destination,
                                      price=price, demandingness=demandingness, availability=availability,
                                      included_in_price=included_in_price,
                                      not_included_in_price=not_included_in_price, state_id=state_id,
                                      )
            self.db.add(arrangement)
            self.db.commit()
            self.db.refresh(arrangement)
            return arrangement
        except IntegrityError as e:
            raise e
        except ValueError as e:
            raise e

    def get_all_arrangements_for_state(self, state_id: str):
        try:
            arrangements = self.db.query(Arrangement).filter(Arrangement.state_id == state_id).all()
            return arrangements
        except Exception as e:
            raise e

    def get_arrangement_by_id(self, arrangement_id: str):
        try:
            arrangement = self.db.query(Arrangement).filter(Arrangement.id == arrangement_id).first()
            return arrangement
        except Exception as e:
            raise e

    def get_arrangement_by_code(self, code: str):
        try:
            arrangement = self.db.query(Arrangement).filter(Arrangement.code == code).first()
            return arrangement
        except Exception as e:
            raise e

    def get_arrangements_under_price(self, price: float):
        try:
            arrangements = self.db.query(Arrangement).filter(Arrangement.price <= price).all()
            return arrangements
        except Exception as e:
            raise e

    def get_arrangements_by_start_date(self, date: str):
        try:
            if date == datetime.strptime(date, "%Y-%m-%d"):
                arrangements = self.db.query(Arrangement).filter(Arrangement.date_of_departure == date).all()
                return arrangements
            raise ValueError
        except ValueError as e:
            raise e
        except Exception as e:
            raise e

    def update_arrangements_price_and_availability(self, arrangement_id: str, price: float, availability: bool):
        try:
            arrangement = self.db.query(Arrangement).filter(Arrangement.id == arrangement_id).first()
            arrangement.price = price
            arrangement.availability = availability
            self.db.add(arrangement)
            self.db.commit()
            self.db.refresh(arrangement)
            return arrangement
        except Exception as e:
            raise e

    def delete_arrangement_by_id(self, arrangement_id: str):
        try:
            arrangement = self.db.query(Arrangement).filter(Arrangement.id == arrangement_id).first()
            if arrangement is None:
                return False
            self.db.delete(arrangement)
            self.db.commit()
            return True
        except Exception as e:
            raise e
