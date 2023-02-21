class ArrangementNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ArrangementAlreadyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ArrangementsNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class DateOfDepartureOrArrivalException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class AccommodationNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class AccommodationAlreadyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ExcursionNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ExcursionAlreadyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class PlanAndProgramNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class PlanAndProgramAlreadyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class InvalidInputException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
