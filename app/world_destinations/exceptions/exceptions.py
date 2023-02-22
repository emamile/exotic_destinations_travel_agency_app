# > This class is used to indicate that a destination was not found in the world
class WorldDestinationNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


# > This exception is raised when a world destination already exists
class WorldDestinationAlreadyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


#
# *|CURSOR_MARCADOR|*
class StateNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


# It creates a new exception class called StateAlreadyExistsException.
class StateAlreadyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


# *|CURSOR_MARCADOR|*
class StateInfoNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


# *|CURSOR_MARCADOR|*
class StateInfoAlreadyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


# > This exception is raised when the state info is not provided
class StateInfoIsMandatoryException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


#
class MandatoryCheckAlreadyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


# *|CURSOR_MARCADOR|*
class MandatoryCheckNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
