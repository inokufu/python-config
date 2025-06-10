class ConfigError(Exception):
    """Base class for package exceptions."""


class UnknownLogLevelError(ConfigError):
    """Raised when a specified log level doesn't match any known log level."""

    def __init__(self, invalid_value: str, valid_values: list) -> None:
        """Raise the error with correct message."""
        super().__init__(
            f"Invalid log level '{invalid_value}'. Must be one of: {valid_values}",
        )
