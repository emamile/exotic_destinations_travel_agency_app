
class UserNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserInvalidPasswordException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserAlreadyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
