# login, destination, direction,

class ElevatorError(Exception):
    """Base class for exceptions in the Elevator system."""
    pass


class LoginError(ElevatorError):
    """raised when incorrect login info is given."""

    def __init__(self):
        self.message = "Cannot login. Incorrect login details provided."
        super().__init__(self.message)


class InvalidDestinationError(ElevatorError):
    """raised when an invalid floor number is given."""

    def __init__(self, floor):
        self.floor = floor
        self.message = f"Invalid floor number: {floor}. Must be between 0 and max floor value."
        super().__init__(self.message)


class NoDirectionError(ElevatorError):
    """raised when no direction can be set."""

    def __init__(self):
        self.message = "Cannot set direction. No floors are selected."
        super().__init__(self.message)


