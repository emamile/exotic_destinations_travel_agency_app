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


class TravelerNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class TravelerAlreadyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class BookedArrangementAlreadyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class BookedArrangementNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class WishListArrangementAlreadyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class WishListArrangementNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class CheckersNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
