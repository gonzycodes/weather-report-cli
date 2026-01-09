import requests
from .config import GEO_BASE_URL, OPENWEATHER_API_KEY, UNITS, LANGUAGE, FORECAST_BASE_URL
from .logger import log_info

def geocode_city(city):
    params = {'q': city, 'limit': 1, 'appid': OPENWEATHER_API_KEY}
    response = requests.get(GEO_BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    if len(data) == 0:
        log_info('List was empty, returning none!')
        return None
    first = data[0]
    return first.get('lat'), first.get('lon'), first.get('name'), first.get('country')


def fetch_forecast(lat, lon):
    params = {'lat': lat, 'lon': lon, 'appid': OPENWEATHER_API_KEY, 'units': UNITS, 'lang': LANGUAGE}
    response = requests.get(FORECAST_BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

def forecast_next_24h(forecast_json):
    items = forecast_json['list']
    return items[:8]

def get_forecast_24h(lat, lon):
    raw = fetch_forecast(lat,lon)
    items_24h = forecast_next_24h(raw)
    return {
        'meta': {
            'lat': lat,
            'lon': lon,
            'provider': 'openweather',
            'type': 'forecast_24h',
            'count': len(items_24h)
        },
        'items' : items_24h
    }
    