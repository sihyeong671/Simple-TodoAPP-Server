from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):

    mysql_user: str
    mysql_password: str
    mysql_host: str
    mysql_port: str
    mysql_db_name: str


    class Confing:
        env_file= '.env'
        env_file_encoding = 'utf-8'


settings = Settings()