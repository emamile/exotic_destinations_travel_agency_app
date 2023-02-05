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
            return travel_agency_repository.get_all_travel_agencies
