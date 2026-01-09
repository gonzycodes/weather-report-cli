#Configuration for paths, constants and app initialization
from pathlib import Path


#Directories and files
THIS_FILE = Path(__file__)

WEATHER_DIR = THIS_FILE.parent

SRC_DIR = WEATHER_DIR.parent

PROJECT_ROOT = SRC_DIR.parent

DATA_DIR = PROJECT_ROOT/'data'

CACHE_DIR = DATA_DIR/'cache'

HISTORY_FILE = DATA_DIR/'history.json'

LOG_DIR = PROJECT_ROOT/'logs'

LOG_FILE = LOG_DIR/'app.log'


#Settings
GEO_BASE_URL = 'http://api.openweathermap.org/geo/1.0/direct'

FORECAST_BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast'

CACHE_EXPIRY_MINUTES = 10

HISTORY_LIMIT = 10

FORECAST_HOURS = 24

TIMEZONE_SETTING = 'auto'

OPENWEATHER_API_KEY = '725d46370f76ce3c31c8826950488f01'

#Adjust this to change behavior, 'INFO' is recommended
LOG_LEVEL_DEFAULT = 'INFO'

UNITS = 'metric'

LANGUAGE = 'eng'

#Creates folders and files if they dont exist
def init_app_dirs():
    paths = [DATA_DIR, CACHE_DIR, LOG_DIR]
    for p in paths:
        p.mkdir(parents=True, exist_ok=True)
    if not HISTORY_FILE.exists():
       HISTORY_FILE.write_text('[]', encoding='utf-8')