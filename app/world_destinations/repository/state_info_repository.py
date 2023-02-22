# Importing the IntegrityError exception from the sqlalchemy.exc module.
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.world_destinations.models.state_info import StateInfo


# > This class is responsible for storing and retrieving state information
class StateInfoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_state_info(self, info_title: str, details: str, state_id: str, is_mandatory: bool = None):
        """
        It creates a new StateInfo object, adds it to the database, commits the changes, and returns the new object

        :param info_title: The title of the information
        :type info_title: str
        :param details: This is the actual information that you want to display to the user
        :type details: str
        :param state_id: The id of the state that the info is associated with
        :type state_id: str
        :param is_mandatory: This is a boolean value that determines whether the information is mandatory or not
        :type is_mandatory: bool
        :return: The info object is being returned.
        """
        try:
            info = StateInfo(info_title=info_title, details=details, is_mandatory=is_mandatory, state_id=state_id)
            self.db.add(info)
            self.db.commit()
            self.db.refresh(info)
            return info
        except IntegrityError as e:
            raise e

    def get_state_infos(self, state_id: str):
        """
        It returns a list of StateInfo objects that have a state_id that matches the state_id passed in

        :param state_id: The state id of the state you want to get the info for
        :type state_id: str
        :return: A list of StateInfo objects
        """
        try:
            infos = self.db.query(StateInfo).filter(StateInfo.state_id == state_id).all()
            return infos
        except Exception as e:
            raise e

    def get_state_info_by_id(self, state_info_id: str):
        """
        It gets a state info object from the database by its id

        :param state_info_id: The id of the state info you want to get
        :type state_info_id: str
        :return: A StateInfo object
        """
        try:
            info = self.db.query(StateInfo).filter(StateInfo.id == state_info_id).first()
            return info
        except Exception as e:
            raise e

    def get_state_info_by_info_title(self, state_id: str, info_title: str):
        """
        It returns the first StateInfo object that matches the state_id and info_title

        :param state_id: str
        :type state_id: str
        :param info_title: The title of the information you want to get
        :type info_title: str
        :return: A list of StateInfo objects
        """
        try:
            info = self.db.query(StateInfo).filter(StateInfo.state_id == state_id, StateInfo.info_title.ilike(f"%{info_title}%")).first()
            return info
        except Exception as e:
            raise e

    def get_all_mandatory_state_infos(self, state_id: str):
        """
        It returns all the mandatory state infos for a given state id

        :param state_id: The id of the state you want to get the info for
        :type state_id: str
        :return: A list of StateInfo objects
        """
        try:
            infos = self.db.query(StateInfo).filter(StateInfo.state_id == state_id, StateInfo.is_mandatory == True).all()
            return infos
        except Exception as e:
            raise e

    def update_state_info(self, state_info_id: str, details: str = None, is_mandatory: bool = None):
        """
        It updates the details and is_mandatory fields of a StateInfo object in the database

        :param state_info_id: The id of the state info you want to update
        :type state_info_id: str
        :param details: str = None, is_mandatory: bool = None
        :type details: str
        :param is_mandatory: This is a boolean value that indicates whether the state is mandatory or not
        :type is_mandatory: bool
        :return: The updated state_info object.
        """
        try:
            info = self.db.query(StateInfo).filter(StateInfo.id == state_info_id).first()
            if info.is_mandatory is None:
                if details is not None:
                    info.details = details
                self.db.add(info)
                self.db.commit()
                self.db.refresh(info)
                return info
            if details is not None:
                info.details = details
            if is_mandatory is not None:
                info.is_mandatory = is_mandatory
            self.db.add(info)
            self.db.commit()
            self.db.refresh(info)
            return info
        except Exception as e:
            raise e

    def delete_state_info_by_id(self, state_info_id: str):
        """
        It deletes a row from the database table StateInfo where the id column matches the state_info_id parameter

        :param state_info_id: The ID of the state information to be deleted
        :type state_info_id: str
        :return: A boolean value.
        """
        try:
            info = self.db.query(StateInfo).filter(StateInfo.id == state_info_id).first()
            if info is None:
                return False
            self.db.delete(info)
            self.db.commit()
            return True
        except Exception as e:
            raise e
