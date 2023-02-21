from sqlalchemy import Null
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.world_destinations.models.useful_info_about_state import UsefulInfoAboutState


class UsefulInfoAboutStateRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_states_useful_info(self, info_title: str, details: str, state_id: str):
        try:
            if info_title == "visa":
                UsefulInfoAboutState.is_visa_needed = False
                useful_info = UsefulInfoAboutState(info_title=info_title, details=details, state_id=state_id)
            elif info_title == "vaccine":
                UsefulInfoAboutState.is_vaccine_needed = False
                useful_info = UsefulInfoAboutState(info_title=info_title, details=details, state_id=state_id)
            elif info_title == "insurance":
                UsefulInfoAboutState.is_insurance_needed = False
                useful_info = UsefulInfoAboutState(info_title=info_title, details=details, state_id=state_id)
            else:
                useful_info = UsefulInfoAboutState(info_title=info_title, details=details, state_id=state_id)
            self.db.add(useful_info)
            self.db.commit()
            self.db.refresh(useful_info)
            return useful_info
        except IntegrityError as e:
            raise e

    def get_states_useful_infos(self, state_id: str):
        try:
            useful_infos = self.db.query(UsefulInfoAboutState).filter(UsefulInfoAboutState.state_id == state_id).all()
            return useful_infos
        except Exception as e:
            raise e

    def get_states_useful_info_by_info_title(self, state_id: str, info_title: str):
        try:
            useful_info = self.db.query(UsefulInfoAboutState).filter(UsefulInfoAboutState.state_id == state_id, UsefulInfoAboutState.info_title.ilike(f"%{info_title}%")).first()
            return useful_info
        except Exception as e:
            raise e

    def update_states_useful_info_detail(self, info_title: str, detail: str, state_id: str):
        try:
            useful_info = self.db.query(UsefulInfoAboutState).filter(UsefulInfoAboutState.state_id == state_id, UsefulInfoAboutState.info_title.ilike(f"%{info_title}%")).first()
            useful_info.detail = detail
            self.db.add(useful_info)
            self.db.commit()
            self.db.refresh(useful_info)
            return useful_info
        except Exception as e:
            raise e

    def update_states_info_about_visa(self, is_visa_needed: bool, state_id: str):
        try:
            useful_info = self.db.query(UsefulInfoAboutState).filter(UsefulInfoAboutState.state_id == state_id, UsefulInfoAboutState.info_title.ilike("%visa%")).first()
            if useful_info:
                useful_info.is_visa_needed = is_visa_needed
                self.db.add(useful_info)
                self.db.commit()
                self.db.refresh(useful_info)
                return useful_info
        except Exception as e:
            raise e

    def update_states_info_about_vaccine(self, is_vaccine_needed: bool, state_id: str):
        try:
            useful_info = self.db.query(UsefulInfoAboutState).filter(UsefulInfoAboutState.state_id == state_id, UsefulInfoAboutState.info_title.ilike("%vaccine%")).first()
            useful_info.is_vaccine_needed = is_vaccine_needed
            self.db.add(useful_info)
            self.db.commit()
            self.db.refresh(useful_info)
            return useful_info
        except Exception as e:
            raise e

    def update_states_info_about_insurance(self, is_insurance_needed: bool, state_id: str):
        try:
            useful_info = self.db.query(UsefulInfoAboutState).filter(UsefulInfoAboutState.state_id == state_id, UsefulInfoAboutState.info_title.ilike("%insurance%")).first()
            useful_info.is_insurance_needed = is_insurance_needed
            self.db.add(useful_info)
            self.db.commit()
            self.db.refresh(useful_info)
            return useful_info
        except Exception as e:
            raise e

    def delete_states_useful_info(self, state_id: str, info_title: str):
        try:
            useful_info = self.db.query(UsefulInfoAboutState).filter(UsefulInfoAboutState.state_id == state_id and UsefulInfoAboutState.info_title == info_title).first()
            if useful_info is None:
                return False
            self.db.delete(useful_info)
            self.db.commit()
            return True
        except Exception as e:
            raise e
