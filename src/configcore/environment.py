from enum import Enum, auto


class Environment(Enum):
    """Represents the different environments in which the application can run."""

    DEVELOPMENT = auto()
    STAGING = auto()
    PRODUCTION = auto()
