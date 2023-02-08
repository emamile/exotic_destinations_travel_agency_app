from pydantic import EmailStr
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
        travel_agencies = TravelAgencyService.get_all_travel_agencies()
        return travel_agencies

    @staticmethod
    def get_travel_agency_by_id(travel_agency_id: str):
        travel_agency = TravelAgencyService.get_travel_agency_by_id(travel_agency_id=travel_agency_id)
        if travel_agency:
            return travel_agency
        else:
            raise HTTPException(status_code=400,
                                detail=f"Travel agency with provided ID {travel_agency_id} does not exist.")

    @staticmethod
    def update_travel_agency_email_and_password(travel_agency_id: str, email: EmailStr, password: str):
        try:
            travel_agency = TravelAgencyService.update_travel_agency_email_and_password(
                travel_agency_id=travel_agency_id, email=email, password=password)
            return travel_agency
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_travel_agency_by_id(travel_agency_id: str):
        try:
            TravelAgencyService.delete_travel_agency_by_id(travel_agency_id=travel_agency_id)
            return Response(content=f"Travel agency with provided ID {travel_agency_id} is deleted.")
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Travel agency with provided ID {travel_agency_id} does not exist.")

