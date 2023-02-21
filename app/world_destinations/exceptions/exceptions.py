class WorldDestinationNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class WorldDestinationAlreadyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class StateNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class StateAlreadyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UsefulInfoAboutStateNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UsefulInfoAboutStateAlreadyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
