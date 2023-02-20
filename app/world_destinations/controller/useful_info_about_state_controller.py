from fastapi import HTTPException, Response
from app.world_destinations.exceptions import StateNotFoundException, UsefulInfoAboutStateNotFoundException, \
    UsefulInfoAboutStateAlreadyExistsException
from app.world_destinations.service import UsefulInfoAboutStateService, StateService


class UsefulInfoAboutStateController:

    @staticmethod
    def create_states_useful_info(info_title: str, details: str, state_id: str):
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            useful_info = UsefulInfoAboutStateService.create_states_useful_info(info_title=info_title,
                                                                                details=details,
                                                                                state_id=state_id)
            return useful_info
        except UsefulInfoAboutStateAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_states_useful_infos(state_id: str):
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            useful_infos = UsefulInfoAboutStateService.get_states_useful_infos(state_id=state_id)
            return useful_infos
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UsefulInfoAboutStateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_states_useful_info_by_info_title(state_id: str, info_title: str):
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            useful_info = UsefulInfoAboutStateService.get_states_useful_info_by_info_title(state_id=state_id,
                                                                                           info_title=info_title)
            return useful_info
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UsefulInfoAboutStateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_states_useful_info_detail(info_title: str, detail: str, state_id: str):
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            useful_info = UsefulInfoAboutStateService.update_states_useful_info_detail(info_title=info_title,
                                                                                       detail=detail,
                                                                                       state_id=state_id)
            return useful_info
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UsefulInfoAboutStateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_states_info_about_visa(state_id: str, is_visa_needed: bool):
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            useful_info = UsefulInfoAboutStateService.update_states_info_about_visa(is_visa_needed=is_visa_needed,
                                                                                    state_id=state_id)
            return useful_info
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UsefulInfoAboutStateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_states_info_about_vaccine(state_id: str, is_vaccine_needed: bool):
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            useful_info = UsefulInfoAboutStateService.update_states_info_about_vaccine(
                                                                                       is_vaccine_needed=is_vaccine_needed,
                                                                                       state_id=state_id)
            return useful_info
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UsefulInfoAboutStateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_states_info_about_insurance(state_id: str, is_insurance_needed: bool):
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            useful_info = UsefulInfoAboutStateService.update_states_info_about_insurance(
                                                                                         is_insurance_needed=is_insurance_needed,
                                                                                         state_id=state_id)
            return useful_info
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UsefulInfoAboutStateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_states_useful_info(state_id: str, info_title: str):
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            if UsefulInfoAboutStateService.delete_states_useful_info(state_id=state_id, info_title=info_title):
                return Response(status_code=200, content=f"Useful info about state with ID {state_id}, with title {info_title} is deleted. ")
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UsefulInfoAboutStateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
