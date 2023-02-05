from sqlalchemy.exc import IntegrityError

from app.travel_agency.services import TravelAgencyService
from fastapi import HTTPException, Response


class TravelAgencyController:

    @staticmethod
    def create_travel_agency(name, email, password, address, telephone_number):
        try:
            travel_agency = TravelAgencyService.create_travel_agency(name=name, email=email, password=password,
                                                                     address=address, telephone_number=telephone_number)
            return travel_agency
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=f"Travel agency with provided email {email} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_travel_agencies():
        return TravelAgencyService.get_all_travel_agencies()
