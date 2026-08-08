from pydantic_settings import BaseSettings, SettingsConfigDict


class Configs(BaseSettings):
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


configs = Configs()
