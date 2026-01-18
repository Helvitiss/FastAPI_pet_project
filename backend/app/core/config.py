from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    database_url: str = 'postgresql+asyncpg://fooddeliveryuser:2213@localhost:6969/fooddeliverydb'
    alembic_url: str = 'postgresql+psycopg2://fooddeliveryuser:2213@localhost:6969/fooddeliverydb'


settings = Settings()


print(settings.database_url)