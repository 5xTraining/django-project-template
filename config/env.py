from collections import ChainMap
from os import environ
from pathlib import Path

from dotenv import dotenv_values

DJANGO_ENV = environ.get("DJANGO_ENV", "local")
ENV = ChainMap(dotenv_values(f".env.{DJANGO_ENV}"), environ)
BASE_DIR = Path(__file__).resolve().parent.parent
