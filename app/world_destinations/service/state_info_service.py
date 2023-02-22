# Importing the IntegrityError exception from the sqlalchemy library.
from sqlalchemy.exc import IntegrityError

from app.database.db import SessionLocal
from app.world_destinations.exceptions import StateInfoAlreadyExistsException, StateInfoNotFoundException
from app.world_destinations.repository.state_info_repository import StateInfoRepository


# > This class provides a service for getting information about the state of the system
class StateInfoService:
    @staticmethod
    def create_state_info(info_title: str, details: str, state_id: str, is_mandatory: bool = None):
        try:
            with SessionLocal() as db:
                state_info_repository = StateInfoRepository(db)
                return state_info_repository.create_state_info(
                    info_title=info_title, details=details, state_id=state_id, is_mandatory=is_mandatory
                )
        except IntegrityError as exc:
            raise StateInfoAlreadyExistsException(
                code=409, message=f"Information with title {info_title} about state with ID {state_id} already exists for this state."
            ) from exc

    @staticmethod
    def get_state_infos(state_id: str):
        """
        It gets the useful information about a state with a given ID

        :param state_id: The ID of the state you want to get the information about
        :type state_id: str
        :return: A list of StateInfo objects
        """
        try:
            with SessionLocal() as db:
                state_info_repository = StateInfoRepository(db)
                infos = state_info_repository.get_state_infos(state_id=state_id)
                if infos:
                    return infos
                raise StateInfoNotFoundException(code=400, message=f"Useful informations about state with ID {state_id} do not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def get_state_info_by_info_title(state_id: str, info_title: str):
        """
        It gets the information about a state by the state ID and the information title

        :param state_id: The ID of the state you want to get information about
        :type state_id: str
        :param info_title: The title of the information you want to get
        :type info_title: str
        :return: A StateInfo object
        """
        try:
            with SessionLocal() as db:
                state_info_repository = StateInfoRepository(db)
                info = state_info_repository.get_state_info_by_info_title(state_id=state_id, info_title=info_title)
                if info:
                    return info
                raise StateInfoNotFoundException(
                    code=400, message=f"Information about state with ID {state_id}, with title {info_title} does not exist."
                )

        except Exception as e:
            raise e

    @staticmethod
    def get_all_mandatory_state_infos(state_id: str):
        """
        It gets all the mandatory state infos for a given state ID

        :param state_id: The ID of the state you want to get the mandatory infos for
        :type state_id: str
        :return: A list of all mandatory state infos.
        """
        try:
            with SessionLocal() as db:
                state_info_repository = StateInfoRepository(db)
                infos = state_info_repository.get_all_mandatory_state_infos(state_id=state_id)
                if infos:
                    return infos
                raise StateInfoNotFoundException(code=400, message=f"State with ID {state_id} does not have any mandatory infos.")
        except Exception as e:
            raise e

    @staticmethod
    def update_state_info(state_info_id: str, details: str = None, is_mandatory: bool = None):
        """
        This function updates the state info details and is_mandatory fields of a state info object in the database

        :param state_info_id: The id of the state info you want to update
        :type state_info_id: str
        :param details: str = None, is_mandatory: bool = None
        :type details: str
        :param is_mandatory: This is a boolean value that indicates whether the state is mandatory or not
        :type is_mandatory: bool
        :return: The updated state info object
        """
        try:
            with SessionLocal() as db:
                state_info_repository = StateInfoRepository(db)
                info = state_info_repository.get_state_info_by_id(state_info_id=state_info_id)
                return state_info_repository.update_state_info(state_info_id=state_info_id, details=details, is_mandatory=is_mandatory)
        except Exception as e:
            raise e

    @staticmethod
    def delete_state_info_by_id(state_info_id: str):
        """
        It deletes the state information by id.

        :param state_info_id: The id of the state information to be deleted
        :type state_info_id: str
        :return: True or False
        """
        try:
            with SessionLocal() as db:
                state_info_repository = StateInfoRepository(db)
                if state_info_repository.delete_state_info_by_id(state_info_id=state_info_id):
                    return True
                raise StateInfoNotFoundException(code=400, message="Information about state does not exist.")
        except Exception as e:
            raise e
