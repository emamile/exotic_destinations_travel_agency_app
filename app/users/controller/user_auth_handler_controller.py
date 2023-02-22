from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.users.services import decode_jwt


# It's a subclass of HTTPBearer that uses the JWT token format
class JWTBearer(HTTPBearer):
    def __init__(self, role: str, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.role = role

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            payload = self.verify_jwt(credentials.credentials)
            if not payload.get("valid"):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            if payload.get("role") != self.role:
                raise HTTPException(status_code=403, detail="User with provided role is not permitted to access this route.")
            return credentials.credentials
        raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> dict:
        """
        It takes a JWT token as a string, decodes it, and returns a dictionary with a key of "valid" and a value of True or
        False, and a key of "role" and a value of the role of the user

        :param jwtoken: The JWT token that you want to verify
        :type jwtoken: str
        :return: A dictionary with the key "valid" and the value of the boolean is_token_valid.
        """
        is_token_valid: bool = False
        try:
            payload = decode_jwt(jwtoken)
        except:
            payload = None
        if payload:
            is_token_valid = True
            return {"valid": is_token_valid, "role": payload["role"]}
        return {"valid": is_token_valid}
