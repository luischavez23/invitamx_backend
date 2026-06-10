from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    FRONTEND_URLS: str

    @property
    def frontend_urls(self):
        return [url.strip() for url in self.FRONTEND_URLS.split(",")]

    class Config:
        env_file = ".env"

settings = Settings()