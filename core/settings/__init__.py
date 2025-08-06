import os
import json
from pathlib import Path
from datetime import timedelta

from dotenv import load_dotenv
from split_settings.tools import include, optional


BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = Path(BASE_DIR, '.env')

load_dotenv(ENV_FILE, override=True)


SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ['DEBUG_MODE']
ALLOWED_HOSTS = [
    '*',
]

settings = ['components/common.py', 'components/database.py', 'components/celery.py']

include(*settings)
