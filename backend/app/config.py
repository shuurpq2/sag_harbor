from pydantic_settings import BaseSettings
from pathlib import Path
from authx import AuthX, AuthXConfig
import socket


hostname = socket.gethostname()
host = socket.gethostbyname(hostname)


script_dir = Path(__file__).parent.absolute()
db_path = script_dir / 'sag_harbour.db'


class Settings(BaseSettings):
    app_name: str = 'sag_harbor'
    debug: bool = True
    database_url: str = f'sqlite:///{db_path}'
    cors_origins: list = [
        'http://localhost:5173',
        'http://localhost:3000',
        'http://127.0.0.1:5173',
        'http://127.0.0.1:3000',
    ] + [f'http://{host}:5173', f'http://{host}:3000']
    static_dir: str = 'static'
    images_dir: str = 'static/images'


    class Config:
        env_file = '.env'


settings = Settings()