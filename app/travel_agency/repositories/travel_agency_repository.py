from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.travel_agency.models import TravelAgency


class TravelAgencyRepository:

    def __init__(self, database: Session):
        self.database = database

    def create_travel_agency(self, name, email, password, address, telephone_number):
        try:
            travel_agency = TravelAgency(name=name, email=email, password=password, address=address,
                                         telephone_number=telephone_number)
            self.database.add(travel_agency)
            self.database.commit()
            self.database.refresh(travel_agency)
            return travel_agency
        except IntegrityError as e:
            raise e

    def get_all_travel_agencies(self):
        return self.database.query(TravelAgency).first()
