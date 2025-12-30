## All paths, all constants and responsible for where all folders are
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
GEO_BASE_URL = '...'

FORECAST_BASE_URL = '...'

CACHE_EXPIRY_MINUTES = 10

HISTORY_LIMIT = 10

FORECAST_HOURS = 24

TIMEZONE_SETTING = 'auto'

#Adjust this to change behavior, 'INFO' is recommended
LOG_LEVEL_DEFAULT = 'INFO'

def init_app_dirs():
    paths = [DATA_DIR, CACHE_DIR, LOG_DIR]
    for p in paths:
        p.mkdir(parents=True, exist_ok=True)
    if not HISTORY_FILE.exists():
       HISTORY_FILE.write_text('[]', encoding='utf-8')