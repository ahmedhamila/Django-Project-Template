import os
import pathlib

from decouple import Config


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
APPS_DIR = BASE_DIR / "app"

config = Config(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = config("SECRET_KEY")
