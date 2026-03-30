from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Smart Notification System Appliance"
    app_version: str = "1.0.0"


settings = Settings()
