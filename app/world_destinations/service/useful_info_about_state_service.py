from sqlalchemy import Null
from sqlalchemy.exc import IntegrityError

from app.database.db import SessionLocal
from app.world_destinations.exceptions import UsefulInfoAboutStateNotFoundException, \
    UsefulInfoAboutStateAlreadyExistsException
from app.world_destinations.repository.useful_info_about_state_repository import UsefulInfoAboutStateRepository


class UsefulInfoAboutStateService:

    @staticmethod
    def create_states_useful_info(info_title: str, details: str, state_id: str):
        try:
            with SessionLocal() as db:
                useful_info_repository = UsefulInfoAboutStateRepository(db)
                return useful_info_repository.create_states_useful_info(info_title=info_title,
                                                                        details=details,
                                                                        state_id=state_id)
        except IntegrityError:
            raise UsefulInfoAboutStateAlreadyExistsException(code=400,
                                                             message=f"Useful information with title {info_title} already exists for this state.")

    @staticmethod
    def get_states_useful_infos(state_id: str):
        try:
            with SessionLocal() as db:
                useful_info_repository = UsefulInfoAboutStateRepository(db)
                useful_infos = useful_info_repository.get_states_useful_infos(state_id=state_id)
                if useful_infos:
                    return useful_infos
                raise UsefulInfoAboutStateNotFoundException(code=400,
                                                            message=f"Useful informations about state with ID {state_id} do not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def get_states_useful_info_by_info_title(state_id: str, info_title: str):
        try:
            with SessionLocal() as db:
                useful_info_repository = UsefulInfoAboutStateRepository(db)
                useful_info = useful_info_repository.get_states_useful_info_by_info_title(state_id=state_id,
                                                                                          info_title=info_title)
                if useful_info:
                    return useful_info
                raise UsefulInfoAboutStateNotFoundException(code=400,
                                                            message=f"Useful information about state with ID {state_id}, with title {info_title} does not exist.")

        except Exception as e:
            raise e

    @staticmethod
    def update_states_useful_info_detail(info_title: str, detail: str, state_id: str):
        try:
            with SessionLocal() as db:
                useful_info_repository = UsefulInfoAboutStateRepository(db)
                useful_info = useful_info_repository.get_states_useful_info_by_info_title(state_id=state_id,
                                                                                          info_title=info_title)
                if useful_info:
                    return useful_info_repository.update_states_useful_info_detail(info_title=info_title,
                                                                                   detail=detail,
                                                                                   state_id=state_id)
                raise UsefulInfoAboutStateNotFoundException(code=400,
                                                            message=f"Useful info about state with ID {state_id}, with title {info_title} does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def update_states_info_about_visa(state_id: str, is_visa_needed: bool):
        try:
            with SessionLocal() as db:
                useful_info_repository = UsefulInfoAboutStateRepository(db)
                useful_info = useful_info_repository.update_states_info_about_visa(state_id=state_id,
                                                                                   is_visa_needed=is_visa_needed)

                if useful_info:
                    return useful_info
                raise UsefulInfoAboutStateNotFoundException(code=400,
                                                            message=f"Useful info about state with ID {state_id}, with title visa does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def update_states_info_about_vaccine(state_id: str, is_vaccine_needed: bool):
        try:
            with SessionLocal() as db:
                useful_info_repository = UsefulInfoAboutStateRepository(db)
                useful_info = useful_info_repository.update_states_info_about_vaccine(state_id=state_id,
                                                                                      is_vaccine_needed=is_vaccine_needed)
                if useful_info:
                    return useful_info
                raise UsefulInfoAboutStateNotFoundException(code=400,
                                                            message=f"Useful info about state with ID {state_id}, with title vaccine does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def update_states_info_about_insurance(state_id: str, is_insurance_needed: bool):
        try:
            with SessionLocal() as db:
                useful_info_repository = UsefulInfoAboutStateRepository(db)
                useful_info = useful_info_repository.update_states_info_about_insurance(state_id=state_id,
                                                                                        is_insurance_needed=is_insurance_needed)
                if useful_info:
                    return useful_info
                raise UsefulInfoAboutStateNotFoundException(code=400,
                                                            message=f"Useful info about state with ID {state_id}, with title insurance does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def delete_states_useful_info(state_id: str, info_title: str):
        try:
            with SessionLocal() as db:
                useful_info_repository = UsefulInfoAboutStateRepository(db)
                if useful_info_repository.delete_states_useful_info(state_id=state_id, info_title=info_title):
                    return True
                raise UsefulInfoAboutStateNotFoundException(code=400,
                                                            message=f"Useful info about state with ID {state_id}, with title {info_title} does not exist.")
        except Exception as e:
            raise e
