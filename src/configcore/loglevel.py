import logging
from enum import IntEnum
from typing import Self

from .errors import UnknownLogLevelError


class LogLevel(IntEnum):
    """Represents the different log levels."""

    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    @classmethod
    def from_str(cls, value: str) -> Self:
        """Create a LogLevel from a string, case-insensitive.

        Args:
            value: String representation of the log level.

        Returns:
            LogLevel enum value.

        Raises:
            UnknownLogLevelError: If the string doesn't match any log level.
        """
        try:
            return cls[value.upper()]
        except KeyError as e:
            valid_values = [e.name for e in cls]
            raise UnknownLogLevelError(value, valid_values) from e
