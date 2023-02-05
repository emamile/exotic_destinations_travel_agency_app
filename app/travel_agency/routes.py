from fastapi import APIRouter
from app.travel_agency.controllers import TravelAgencyController
from app.travel_agency.schemas.travel_agency_schema import *

travel_agency_router = APIRouter(tags=["TRAVEL AGENCY"], prefix="/api/travel_agency")


@travel_agency_router.post("/create-travel-agency", response_model=TravelAgencySchema)
def create_travel_agency(travel_agency: TravelAgencySchemaIn):
    return TravelAgencyController.create_travel_agency(name=travel_agency.name, email=travel_agency.email,
                                                       password=travel_agency.password, address=travel_agency.address,
                                                       telephone_number=travel_agency.telephone_number)


@travel_agency_router.get("/get-all-travel-agencies", response_model=list[TravelAgencySchema])
def get_all_travel_agencies():
    return TravelAgencyController.get_all_travel_agencies()
