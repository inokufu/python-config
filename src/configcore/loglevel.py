import logging
from enum import IntEnum
from typing import Self


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
            ValueError: If the string doesn't match any log level.
        """
        try:
            return cls[value.upper()]
        except KeyError as e:
            valid_values = [e.name for e in cls]
            raise ValueError(
                f"Invalid log level '{value}'. Must be one of: {valid_values}",
            ) from e
