from fastapi import APIRouter, HTTPException
from pydantic import EmailStr

from app.travel_agency.controllers import TravelAgencyController
from app.travel_agency.schemas.travel_agency_schema import TravelAgencySchema, TravelAgencySchemaIn

travel_agency_router = APIRouter(tags=["TRAVEL AGENCY"], prefix="/api/travel_agency")


@travel_agency_router.post("/create-travel-agency", response_model=TravelAgencySchema)
def create_travel_agency(travel_agency: TravelAgencySchemaIn):
    return TravelAgencyController.create_travel_agency(name=travel_agency.name, email=travel_agency.email,
                                                       password=travel_agency.password, address=travel_agency.address,
                                                       telephone_number=travel_agency.telephone_number)


@travel_agency_router.get("/get-all-travel-agencies", response_model=list[TravelAgencySchema])
def get_all_travel_agencies():
    return TravelAgencyController.get_all_travel_agencies()


@travel_agency_router.get("/get-travel-agency-by-id", response_model=TravelAgencySchema)
def get_travel_agency_by_id(travel_agency_id: str):
    return TravelAgencyController.get_travel_agency_by_id(travel_agency_id=travel_agency_id)


@travel_agency_router.put("/update/email-and-password", response_model=TravelAgencySchema)
def update_travel_agency_email_and_password(travel_agency_id: str, email: EmailStr, password: str):
    return TravelAgencyController.update_travel_agency_email_and_password(travel_agency_id=travel_agency_id,
                                                                          email=email, password=password)

@travel_agency_router.delete("/delete-travel-agency-by-id")
def delete_travel_agency_by_id(travel_agency_id: str):
    return TravelAgencyController.delete_travel_agency_by_id(travel_agency_id=travel_agency_id)

