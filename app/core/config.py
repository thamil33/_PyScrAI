"""
Configuration settings for ScrAI API
"""
import os
from typing import List, Union
from pydantic import AnyHttpUrl, computed_field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    # Project Info
    PROJECT_NAME: str = "ScrAI"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "AI SoulSculpting Platform with LLM Integration and CLI Interface"
    API_V1_STR: str = "/api/v1"

    # CORS
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @model_validator(mode="after")
    def assemble_cors_origins(self) -> "Settings":
        if isinstance(self.BACKEND_CORS_ORIGINS, str):
            self.BACKEND_CORS_ORIGINS = [
                i.strip() for i in self.BACKEND_CORS_ORIGINS.split(",")
            ]
        return self

    # Database
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_DB: str = "scriptorium"
    POSTGRES_PORT: int = 5432

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    # LLM Configuration
    LLM_API_PROVIDER: str = "openrouter"  # Options: openrouter, lmproxy, lmstudio
    DEFAULT_MODEL: str = "openai/gpt-4o-mini"

    # OpenRouter Settings
    OPENROUTER_API_KEY: str = ""
    OPENROUTER_XTRA_URL: str = ""
    OPENROUTER_XTRA_TITLE: str = ""

    # LM Studio / LMProxy Settings
    LM_STUDIO_URL: str = "http://127.0.0.1:1234/v1"
    LM_STUDIO_API_KEY: str = "lm-studio"

    # Server Settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True

    # CLI Settings
    CLI_HISTORY_FILE: str = ".scrai_history"
    CLI_CONFIG_FILE: str = ".scrai_config.json"


# Create global settings instance
settings = Settings()
