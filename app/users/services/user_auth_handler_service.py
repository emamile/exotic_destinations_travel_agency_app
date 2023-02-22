# It's importing the time module.
import time
from typing import Dict

import jwt

from app.config import settings

USER_SECRET = settings.USER_SECRET
JWT_ALGORITHM = settings.ALGORITHM


def sign_jwt(user_id: str, role: str) -> Dict[str, str]:
    """
    It creates a JWT with a user_id, role, and expiration time, and then returns it

    :param user_id: The user's ID
    :type user_id: str
    :param role: The role of the user. This is used to determine what the user can do
    :type role: str
    :return: A dictionary with a key of access_token and a value of the token.
    """
    payload = {"user_id": user_id, "role": role, "expires": time.time() + 2400}
    token = jwt.encode(payload, USER_SECRET, algorithm=JWT_ALGORITHM)
    return {"access_token": token}


def decode_jwt(token: str) -> dict:
    """
    It decodes the token and returns the decoded token if it's not expired, otherwise it returns an empty dictionary

    :param token: The token to decode
    :type token: str
    :return: A dictionary with the user's information.
    """
    try:
        decoded_token = jwt.decode(token, USER_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except Exception:
        return {}
