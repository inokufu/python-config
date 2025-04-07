from abc import ABC, abstractmethod

from .environment import Environment
from .loglevel import LogLevel


class ConfigContract(ABC):
    """Abstract base class defining the contract for configuration management."""

    @abstractmethod
    def get_log_level(self) -> LogLevel:
        """Get the log level.

        Returns:
            LogLevel: The log level.
        """
        raise NotImplementedError

    @abstractmethod
    def get_environment(self) -> Environment:
        """Get the current environment.

        Returns:
            Environment: The current environment.
        """
        raise NotImplementedError

    def is_env_production(self) -> bool:
        """Check if the current environment is Production.

        Returns:
            bool: True if current environment is Production.
        """
        return self.get_environment() == Environment.PRODUCTION
