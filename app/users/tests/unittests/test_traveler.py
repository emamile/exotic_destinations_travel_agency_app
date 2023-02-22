# Importing the pytest module.
import pytest
from sqlalchemy.exc import IntegrityError

from app.tests import TestClass, TestingSessionLocal
from app.users.repository import TravelerRepository, UserRepository


# This class tests the TravelerRepo class.
class TestTravelerRepo(TestClass):
    def create_travelers_for_methods(self):
        """
        It creates 4 users and 4 travelers, each traveler is linked to a user
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            traveler_repository = TravelerRepository(db)
            user1 = user_repository.create_user(email="user1@gmail.com", password="123")
            user2 = user_repository.create_user(email="user2@gmail.com", password="123")
            user3 = user_repository.create_user(email="user3@gmail.com", password="123")
            user4 = user_repository.create_user(email="user4@gmail.com", password="123")

            traveler = traveler_repository.create_traveler(
                name="traveler", surname="surname", telephone_number="123", passport_number="123", user_id=user1.id
            )
            traveler = traveler_repository.create_traveler(
                name="traveler", surname="surname", telephone_number="123", passport_number="1234", user_id=user2.id
            )
            traveler = traveler_repository.create_traveler(
                name="traveler", surname="surname", telephone_number="123", passport_number="12345", user_id=user3.id
            )
            traveler = traveler_repository.create_traveler(
                name="traveler", surname="surname", telephone_number="123", passport_number="123456", user_id=user4.id
            )

    def test_create_traveler(self):
        """
        It creates a user, then creates a traveler with the user's id
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            traveler_repository = TravelerRepository(db)
            user = user_repository.create_user(email="user1@gmail.com", password="123")
            traveler = traveler_repository.create_traveler(
                name="traveler", surname="surname", telephone_number="123", passport_number="123", user_id=user.id
            )
            assert traveler.name == "traveler"
            assert traveler.surname == "surname"
            assert traveler.telephone_number == "123"
            assert traveler.passport_number == "123"
            assert traveler.user_id == user.id

    def test_create_traveler_error(self):
        """
        The function creates a user and a traveler, and then tries to create another traveler with the same passport number,
        which should raise an IntegrityError
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            traveler_repository = TravelerRepository(db)
            user = user_repository.create_user(email="user1@gmail.com", password="123")
            traveler = traveler_repository.create_traveler(
                name="traveler", surname="surname", telephone_number="123", passport_number="123", user_id=user.id
            )
            assert not traveler.name != "traveler"
            assert not traveler.surname != "surname"
            assert not traveler.telephone_number != "123"
            assert not traveler.passport_number != "123"
            assert not traveler.user_id != user.id
            with pytest.raises(IntegrityError):
                traveler1 = traveler_repository.create_traveler(
                    name="traveler", surname="surname", telephone_number="123", passport_number="123", user_id=user.id
                )

    def test_get_all_travelers(self):
        """
        It creates four travelers, then it gets all the travelers from the database and asserts that the length of the list
        of travelers is four
        """
        self.create_travelers_for_methods()
        with TestingSessionLocal() as db:
            traveler_repository = TravelerRepository(db)
            all_travelers = traveler_repository.get_all_travelers()
            assert len(all_travelers) == 4

    def test_get_all_travelers_error(self):
        """
        This function tests the get_all_travelers() method in the TravelerRepository class
        """
        self.create_travelers_for_methods()
        with TestingSessionLocal() as db:
            traveler_repository = TravelerRepository(db)
            all_travelers = traveler_repository.get_all_travelers()
            assert not len(all_travelers) != 4

    def test_get_traveler_by_id(self):
        """
        It creates a user, creates a traveler, and then gets the traveler by id
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(email="user1@gmail.com", password="123")
            traveler_repository = TravelerRepository(db)
            traveler = traveler_repository.create_traveler(
                name="traveler", surname="surname", telephone_number="123", passport_number="123", user_id=user.id
            )
            traveler1 = traveler_repository.get_traveler_by_id(traveler_id=traveler.id)
            assert traveler == traveler1

    def test_get_traveler_by_id_error(self):
        """
        It checks if the traveler is not equal to traveler1.
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(email="user1@gmail.com", password="123")
            traveler_repository = TravelerRepository(db)
            traveler = traveler_repository.create_traveler(
                name="traveler", surname="surname", telephone_number="123", passport_number="123", user_id=user.id
            )
            traveler1 = traveler_repository.get_traveler_by_id(traveler_id=traveler.id)
            assert not traveler != traveler1

    def test_get_traveler_by_passport_number(self):
        """
        It creates a user and a traveler, then it gets the traveler by passport number.
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user@gmail.com", "123")
            traveler_repository = TravelerRepository(db)
            traveler = traveler_repository.create_traveler(
                name="traveler", surname="surname", telephone_number="123", passport_number="123", user_id=user.id
            )
            traveler1 = traveler_repository.get_traveler_by_passport_number(passport_number=traveler.passport_number)
            assert traveler == traveler1

    def test_get_traveler_by_passport_number_error(self):
        """
        It checks if the traveler is not equal to traveler1.
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user@gmail.com", "123")
            traveler_repository = TravelerRepository(db)
            traveler = traveler_repository.create_traveler(
                name="traveler", surname="surname", telephone_number="123", passport_number="123", user_id=user.id
            )
            traveler1 = traveler_repository.get_traveler_by_passport_number(passport_number=traveler.passport_number)
            assert not traveler != traveler1

    def test_update_traveler(self):
        """
        It updates the traveler's information.
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user@gmail.com", "1234")
            traveler_repository = TravelerRepository(db)
            traveler = traveler_repository.create_traveler(
                name="traveler", surname="surname", telephone_number="123", passport_number="123", user_id=user.id
            )
            traveler = traveler_repository.update_traveler(
                traveler_id=traveler.id,
                surname=traveler.surname,
                telephone_number=traveler.telephone_number,
                passport_number=traveler.passport_number,
            )
            assert traveler.surname == "surname"
            assert traveler.telephone_number == "123"
            assert traveler.passport_number == "123"

    def test_update_traveler_error(self):
        """
        It tests the update_traveler function.
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user@gmail.com", "1234")
            traveler_repository = TravelerRepository(db)
            traveler = traveler_repository.create_traveler(
                name="traveler", surname="surname", telephone_number="123", passport_number="123", user_id=user.id
            )
            traveler = traveler_repository.update_traveler(
                traveler_id=traveler.id,
                surname=traveler.surname,
                telephone_number=traveler.telephone_number,
                passport_number=traveler.passport_number,
            )
            assert not traveler.surname != "surname"
            assert not traveler.telephone_number != "123"
            assert not traveler.passport_number != "123"
