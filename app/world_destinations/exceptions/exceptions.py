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
