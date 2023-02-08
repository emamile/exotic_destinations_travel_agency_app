from pydantic import EmailStr

from app.database.db import SessionLocal
from app.travel_agency.repositories import TravelAgencyRepository


class TravelAgencyService:

    @staticmethod
    def create_travel_agency(name, email, password, address, telephone_number):
        with SessionLocal() as db:
            try:
                travel_agency_repository = TravelAgencyRepository(db)
                return travel_agency_repository.create_travel_agency(name=name, email=email, password=password,
                                                                     address=address, telephone_number=telephone_number)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_travel_agencies():
        with SessionLocal() as db:
            travel_agency_repository = TravelAgencyRepository(db)
            return travel_agency_repository.get_all_travel_agencies()

    @staticmethod
    def get_travel_agency_by_id(travel_agency_id: str):
        with SessionLocal() as db:
            travel_agency_repository = TravelAgencyRepository(db)
            return travel_agency_repository.get_travel_agency_by_id(travel_agency_id=travel_agency_id)

    @staticmethod
    def update_travel_agency_email_and_password(travel_agency_id: str, email: EmailStr, password: str):
        with SessionLocal() as db:
            try:
                travel_agency_repository = TravelAgencyRepository(db)
                return travel_agency_repository.update_travel_agency_email_and_password(
                    travel_agency_id=travel_agency_id, email=email, password=password)
            except Exception as e:
                raise e

    @staticmethod
    def delete_travel_agency_by_id(travel_agency_id: str):
        try:
            with SessionLocal() as db:
                travel_agency_repository = TravelAgencyRepository(db)
                return travel_agency_repository.delete_travel_agency_by_id(travel_agency_id=travel_agency_id)
        except Exception as e:
            raise e

