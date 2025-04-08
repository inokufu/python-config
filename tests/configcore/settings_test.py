import os

import pytest
from pydantic import ValidationError
from pydantic_settings import SettingsConfigDict

from src.configcore import Environment, LogLevel, Settings


class TestSettings:
    """Test suite for Settings class."""

    def setup_method(self) -> None:
        """Set up test environment by clearing env vars and preventing .env loading."""
        self.original_env = dict(os.environ)
        os.environ.clear()

        # Save the original configuration
        self.original_config = Settings.model_config

        # Disable .env loading during tests
        Settings.model_config = SettingsConfigDict(env_file=None)

    def teardown_method(self) -> None:
        """Restore original environment and configuration."""
        Settings.model_config = self.original_config
        os.environ.update(self.original_env)

    def test_default_values(self) -> None:
        """Test that settings loads with correct default values."""
        settings = Settings()
        assert settings.get_environment() == Environment.PRODUCTION
        assert settings.get_log_level() == LogLevel.INFO

    def test_environment_override(self) -> None:
        """Test that environment variables override defaults."""
        os.environ.update(
            {
                "ENVIRONMENT": "development",
                "LOG_LEVEL": "debug",
            },
        )

        settings = Settings()
        assert settings.get_environment() == Environment.DEVELOPMENT
        assert settings.get_log_level() == LogLevel.DEBUG

    def test_invalid_environment(self) -> None:
        """Test that invalid environment raises error."""
        os.environ["ENVIRONMENT"] = "invalid"

        with pytest.raises(KeyError):
            Settings()

    def test_invalid_log_level(self) -> None:
        """Test that invalid log level raises error."""
        os.environ["LOG_LEVEL"] = "invalid"

        with pytest.raises(ValidationError) as exc_info:
            Settings()
        assert "log_level" in str(exc_info.value)
        assert len(exc_info.value.errors()) == 1

    def test_is_env_production(self) -> None:
        """Test is_env_production helper method."""
        settings = Settings(environment=Environment.PRODUCTION)
        assert settings.is_env_production() is True

        settings = Settings(environment=Environment.DEVELOPMENT)
        assert settings.is_env_production() is False

    def test_case_insensitive_values(self) -> None:
        """Test case insensitivity for environment and log level."""
        os.environ.update(
            {
                "ENVIRONMENT": "DeVelOpMeNt",
                "LOG_LEVEL": "DeBuG",
            },
        )

        settings = Settings()
        assert settings.get_environment() == Environment.DEVELOPMENT
        assert settings.get_log_level() == LogLevel.DEBUG
