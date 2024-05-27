from pathlib import Path
from dotenv import dotenv_values

ENV = dotenv_values(".env")
DJANGO_ENV = ENV.get("DJANGO_ENV", "development")
BASE_DIR = Path(__file__).resolve().parent.parent
