# ConfigCore

[![Python](https://img.shields.io/badge/Python-FFD43B?logo=python)](https://www.python.org/)
![License](https://img.shields.io/badge/GPL--3.0-red?logo=gnu)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-E6F0FF?logo=githubactions)](https://github.com/features/actions)
[![Pytest](https://img.shields.io/badge/pytest-E6F7FF?logo=pytest)](https://docs.pytest.org/)
[![EditorConfig](https://img.shields.io/badge/EditorConfig-333333?logo=editorconfig)](https://editorconfig.org/)
[![Rye](https://img.shields.io/badge/Rye-000000?logo=rye)](https://rye.astral.sh/)
[![Ruff](https://img.shields.io/badge/Ruff-3A3A3A?logo=ruff)](https://docs.astral.sh/ruff/)
[![Pre-commit](https://img.shields.io/badge/pre--commit-40332E?logo=pre-commit)](https://pre-commit.com/)
[![Makefile](https://img.shields.io/badge/Makefile-427819?logo=gnu)](https://www.gnu.org/software/make/manual/make.html)
[![MkDocs](https://img.shields.io/badge/MkDocs-526CFE?logo=markdown)](https://www.mkdocs.org/)

## Overview

ConfigCore provides a minimal, type-safe foundation for building configuration
systems in Python applications. Rather than being a complete configuration
solution, it defines contracts and base classes that can be extended to create
application-specific configuration systems.

The library focuses on:

- 🔄 Providing a standardized way to handle environment selection
- 📊 Managing log levels consistently across projects
- 🧩 Offering a base Settings class for extension
- 📝 Using Pydantic for type validation and .env file loading

## Setup and installation

### Prerequisites

- Python 3.12 or higher
- [Rye](https://rye.astral.sh) for dependency management

### Installation

1. Clone the repository

2. Install dependencies
   ```sh
   make init
   ```

## Usage

### Extending the Base Settings

ConfigCore is designed to be extended in your projects. Here's how to use it:

```python
from configcore import Settings
from pydantic import Field


class MyAppSettings(Settings):
  """Application-specific settings extending the base Settings class."""

  # Add your application-specific settings
  api_url: str = Field(default="https://api.example.com")
  max_retry_count: int = Field(default=3, ge=1)
  timeout_seconds: float = Field(default=30.0)

  # Add custom methods as needed
  def get_api_timeout(self) -> float:
    if self.is_env_production():
      return self.timeout_seconds
    return self.timeout_seconds * 2
```

### Using Your Configuration

```python
# In your application
settings = MyAppSettings()  # Loads from environment variables / .env

# Access standard settings from the base class
env = settings.get_environment()  # Returns Environment enum
log_level = settings.get_log_level()  # Returns LogLevel enum
is_prod = settings.is_env_production()  # Convenience method

# Access your custom settings
api_url = settings.api_url
timeout = settings.get_api_timeout()
```

## Development

### Code Formatting and Linting

This project uses ruff for formatting and linting:

```sh
# Format code
make format

# Run linters
make lint
```

### Running Tests

```sh
# Run tests with coverage
make test
```

### Environment Variables

| Variable    | Description             | Default Value | Possible Values                       |
|-------------|-------------------------|---------------|---------------------------------------|
| ENVIRONMENT | Application environment | PRODUCTION    | DEVELOPMENT, STAGING, PRODUCTION      |
| LOG_LEVEL   | Logging level           | INFO          | DEBUG, INFO, WARNING, ERROR, CRITICAL |

## Contributing

We welcome contributions to this project! Please see
the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to
contribute, including:

- How to set up your development environment
- Coding standards and style guidelines
- Pull request process
- Testing requirements

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0) -
see the LICENSE file for details.

GPL-3.0 is a strong copyleft license that requires anyone who distributes your
code or a derivative work to make the source available under the same terms.
