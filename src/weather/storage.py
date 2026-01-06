from pathlib import Path
import json
from datetime import datetime as dt
from .config import CACHE_DIR
##  Read and Write JSON, cache, history, (no api code)
def get_cache_path(lat, lon):
    rounded_lat = round(float(lat), 3)
    rounded_lon = round(float(lon), 3)
    file_name = (f'{rounded_lat}_{rounded_lon}.json')
    return CACHE_DIR/file_name

def save_cache(lat, lon, data):
    cache_path = get_cache_path(lat,lon)
    payload = {
     'meta':{
         'fetched_at': dt.now().isoformat(),
         'lat': lat,
         'lon': lon
         },
     'data':{
         'weather_data': data
     }  
    }
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    with open(cache_path, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2)