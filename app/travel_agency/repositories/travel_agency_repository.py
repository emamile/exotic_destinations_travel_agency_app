from pydantic import EmailStr
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.travel_agency.models import TravelAgency


class TravelAgencyRepository:
    def __init__(self, database: Session):
        self.database = database

    def create_travel_agency(self, name, email, password, address, telephone_number):
        try:
            travel_agency = TravelAgency(
                name=name, email=email, password=password, address=address, telephone_number=telephone_number
            )
            self.database.add(travel_agency)
            self.database.commit()
            self.database.refresh(travel_agency)
            return travel_agency
        except IntegrityError as e:
            raise e

    def get_all_travel_agencies(self):
        travel_agencies = self.database.query(TravelAgency).all()
        return travel_agencies

    def get_travel_agency_by_id(self, travel_agency_id: str):
        travel_agency = self.database.query(TravelAgency).filter(TravelAgency.id == travel_agency_id).first()
        return travel_agency

    def update_travel_agency_email_and_password(self, travel_agency_id: str, email: EmailStr, password: str):
        try:
            travel_agency = self.database.query(TravelAgency).filter(TravelAgency.id == travel_agency_id).first()
            travel_agency.email = email
            travel_agency.password = password
            self.database.add(travel_agency)
            self.database.commit()
            self.database.refresh(travel_agency)
            return travel_agency
        except Exception as e:
            raise e

    def delete_travel_agency_by_id(self, travel_agency_id: str):
        try:
            travel_agency = self.database.query(TravelAgency).filter(TravelAgency.id == travel_agency_id).first()
            self.database.delete(travel_agency)
            self.database.commit()
            return True
        except Exception as e:
            raise e
