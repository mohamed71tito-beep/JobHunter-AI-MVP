from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "JobHunter AI"

    database_url: str = "sqlite:///./jobhunter.db"
    cors_origins: str = "http://localhost:3000"

    telegram_bot_token: str = ""
    ai_api_key: str = ""

    adzuna_app_id: str = ""
    adzuna_app_key: str = ""
    adzuna_country: str = "eg"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()