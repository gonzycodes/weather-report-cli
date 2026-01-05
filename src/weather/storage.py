from pathlib import Path

from .config import CACHE_DIR
##  Read and Write JSON, cache, history, (no api code)
def get_cache_path(lat,lon):
    rounded_lat = round(float(lat), 3)
    rounded_lon = round(float(lon), 3)
    file_name = (f'{rounded_lat}_{rounded_lon}.json')
    return CACHE_DIR/file_name