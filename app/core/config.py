from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    app_name: str = "User Api"
    ACCESS_KEY_ID: str
    SECRET_ACCESS_ID: str
    BUCKET_NAME: str
    SEARCH_API: str

    MGDB_USERNAME: str
    MGDB_PASSWORD: str
    MGDB_HOST: str
    MGDB_DB: str
    MONGODB_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
