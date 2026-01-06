# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2026-01-06

### Changed

- Python version to 3.14
- Migrated from Rye to uv
- Type checking with ty


## [0.2.0] - 2025-07-17

### Changed

- Python version to 3.13
- Upgrade dependencies


## [0.1.0] - 2025-03-20

### Added

- Initial release of the configuration library
- ConfigContract abstract base class defining the configuration interface
- Environment enum with DEVELOPMENT, STAGING, and PRODUCTION options
- LogLevel enum mapping to standard Python logging levels
- Settings class using Pydantic for environment variable loading
- Support for .env file configuration
- Type-safe configuration with validation
- Helper methods for environment checking

