"""This file contains pytest fixtures available to all tests.

Fixtures are functions that pytest runs before tests to set up preconditions.
pytest automatically discovers this file and makes fixtures available
to all test modules without needing to import them.
"""

from unittest.mock import Mock

import pytest

from src.configcore.contract import ConfigContract


@pytest.fixture
def mock_config() -> Mock:
    """Create a mock config.

    :return: A mock config conforming to ConfigContract
    """
    return Mock(spec=ConfigContract)
