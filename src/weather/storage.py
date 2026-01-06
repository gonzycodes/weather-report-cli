import json
from datetime import datetime as dt
from .config import CACHE_DIR, CACHE_EXPIRY_MINUTES
from .logger import log_info, log_exception
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
        
def load_cache(lat, lon):
    cache_path = get_cache_path(lat, lon)
    if not cache_path.is_file():
        log_info('Cache miss (no file)')
        return None
    try:
        with open(cache_path, 'r' ,encoding='utf-8') as f:
          payload = json.load(f)
          fetched_at = payload['meta']['fetched_at']
          fetched_dt = dt.fromisoformat(fetched_at)
          now = dt.now()
          age = now - fetched_dt
          age_in_minutes = age.total_seconds() / 60
          if age_in_minutes <= CACHE_EXPIRY_MINUTES:
             log_info('Cache hit')
             return payload['data']['weather_data']
          else:
             log_info('Cache expired')
             return None
    except Exception:
        log_exception('Load cache failed')
        return None