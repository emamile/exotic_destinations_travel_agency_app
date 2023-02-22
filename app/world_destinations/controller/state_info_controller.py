# Importing the HTTPException and Response classes from the fastapi module.
from fastapi import HTTPException, Response

from app.world_destinations.exceptions import StateInfoAlreadyExistsException, StateInfoNotFoundException, StateNotFoundException
from app.world_destinations.service import StateInfoService, StateService


# > This class is responsible for handling the state information of the game
class StateInfoController:
    @staticmethod
    def create_state_info(info_title: str, details: str, state_id: str, is_mandatory: bool = None):
        """
        It creates a state info object and returns it

        :param info_title: The title of the information
        :type info_title: str
        :param details: The details of the state info
        :type details: str
        :param state_id: The id of the state to which the info is to be added
        :type state_id: str
        :param is_mandatory: This is a boolean value that determines whether the state info is mandatory or not
        :type is_mandatory: bool
        :return: A state info object
        """
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            info = StateInfoService.create_state_info(info_title=info_title, details=details, is_mandatory=is_mandatory, state_id=state_id)
            return info
        except StateInfoAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_state_infos(state_id: str):
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            infos = StateInfoService.get_state_infos(state_id=state_id)
            return infos
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except StateInfoNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_state_info_by_info_title(state_id: str, info_title: str):
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            info = StateInfoService.get_state_info_by_info_title(state_id=state_id, info_title=info_title)
            return info
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except StateInfoNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_mandatory_state_infos(state_id: str):
        try:
            state = StateService.get_state_by_id(state_id=state_id)
            infos = StateInfoService.get_all_mandatory_state_infos(state_id=state_id)
            return infos
        except StateNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except StateInfoNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def update_state_info(state_info_id: str, details: str = None, is_mandatory: bool = None):
        try:
            info = StateInfoService.update_state_info(state_info_id=state_info_id, details=details, is_mandatory=is_mandatory)
            return info
        except StateInfoNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_state_info_by_id(state_info_id: str):
        try:
            if StateInfoService.delete_state_info_by_id(state_info_id=state_info_id):
                return Response(status_code=200, content="Information about state is deleted. ")
        except StateInfoNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
