
import logging

from pydantic_settings import BaseSettings, SettingsConfigDict

# One logger for this file/module
logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    """
    Central place for application configuration.

    All four values must be supplied through environment variables
    or the .env file. Missing values will cause a validation error.
    """

    app_name: str
    base_url: str
    database_url: str
    redis_url: str

    # Tell Pydantic Settings to read the .env file.
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


# Create one settings object for the application to reuse.
settings = Settings()

logger.info("Application settings loaded")
