# Importing the pytest module.
import pytest
from sqlalchemy.exc import IntegrityError

from app.tests import TestClass, TestingSessionLocal
from app.users.repository import UserRepository


# > This class tests the user repository
class TestUserRepo(TestClass):
    def create_users_for_methods(self):
        """
        It creates 4 users in the database
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(email="user1@gmail.com", password="123")
            user = user_repository.create_user(email="user2@gmail.com", password="123")
            user = user_repository.create_user(email="user3@gmail.com", password="123")
            user = user_repository.create_user(email="user4@gmail.com", password="123")

    def test_create_user(self):
        """
        Create a user and assert that the email and is_superuser fields are correct.
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(email="user@gmail.com", password="123")
            assert user.email == "user@gmail.com"
            assert user.is_superuser is False

    def test_create_user_error(self):
        """
        It creates a user and checks if the user is a superuser. If the user is not a superuser, it raises an
        IntegrityError.
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(email="user@gmail.com", password="123")
            assert user.is_superuser is not True
            with pytest.raises(IntegrityError):
                user1 = user_repository.create_user(email="user@gmail.com", password="123")

    def test_create_super_user(self):
        """
        > Create a super user with the email "superuser@gmail.com" and password "1234" and assert that the email and
        is_superuser attributes are correct
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            super_user = user_repository.create_super_user(email="superuser@gmail.com", password="1234")
            assert super_user.email == "superuser@gmail.com"
            assert super_user.is_superuser is True

    def test_create_super_user_error(self):
        """
        It creates a super user and checks if the user is a super user.
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            super_user = user_repository.create_super_user(email="superuser@gmail.com", password="1234")
            assert super_user.is_superuser is not False
            with pytest.raises(IntegrityError):
                user1 = user_repository.create_super_user(email="superuser@gmail.com", password="1234")

    def test_get_all_users(self):
        """
        It creates a user repository and then gets all the users from the database.
        """
        self.create_users_for_methods()
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            all_users = user_repository.get_all_users()
            assert len(all_users) == 4

    def test_get_all_users_error(self):
        """
        It tests that the get_all_users() method returns the correct number of users.
        """
        self.create_users_for_methods()
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            all_users = user_repository.get_all_users()
            assert not len(all_users) != 4

    def test_get_user_by_id(self):
        """
        It creates a user, then gets the user by id and asserts that the user created is the same as the user retrieved
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(email="user@gmail.com", password="123")
            user1 = user_repository.get_user_by_id(user_id=user.id)
            assert user == user1

    def test_get_user_by_id_error(self):
        """
        It tests if the user is not equal to user1.
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(email="user@gmail.com", password="123")
            user1 = user_repository.get_user_by_id(user_id=user.id)
            assert not user != user1

    def test_get_user_by_email(self):
        """
        It creates a user with email and password and then gets the user by email.
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("user@gmail.com", "123")
            user1 = user_repository.get_user_by_email(email="user@gmail.com")
            assert user == user1

    def test_get_user_by_email_error(self):
        """
        It tests if the user is created and if the user is retrieved by email.
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(email="user@gmail.com", password="123")
            user1 = user_repository.get_user_by_email(email="user@gmail.com")
            assert not user != user1

    def test_update_users_email_and_password(self):
        """
        It updates the email and password of a user.
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(email="user@gmail.com", password="1234")
            user = user_repository.update_users_email_and_password(user_id=user.id, email="user1@gmail.com", password="12345")
            assert user.email == "user1@gmail.com"
            assert user.password == "12345"

    def test_update_users_email_and_password_error(self):
        """
        It updates the user's email and password.
        """
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(email="user@gmail.com", password="1234")
            user = user_repository.update_users_email_and_password(user_id=user.id, email="user1@gmail.com", password="12345")
            assert not user.email != "user1@gmail.com"
            assert not user.password != "12345"
