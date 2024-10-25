import typing
import packaging.version

PROJECT_API_URL: str | None = None
"""e.g. https://www.example.com"""
API_SERVER_VERSION: typing.Final[packaging.version.Version] = packaging.version.Version(
    "4.0.0"
)
"""Implemented API Server version"""
del typing
