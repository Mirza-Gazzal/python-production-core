from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Python Core"
    env: str = "dev"
    host: str = "127.0.0.1"
    port: int = 8000

    # keep it as a string in .env
    cors_origins: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    def cors_origins_list(self) -> list[str]:
        """
        Convert comma-separated CORS origins into a list safely.
        """
        if not self.cors_origins.strip():
            return []
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


settings = Settings()
