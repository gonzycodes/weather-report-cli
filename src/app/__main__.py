from weather.logger import setup_logger, log_info, log_error
from weather.config import init_app_dirs
from weather.client import geocode_city, get_forecast_24h
from weather.storage import load_cache, save_cache, append_history
from app.cli import ask_for_city, print_forecast

from datetime import datetime as dt

def main():
    setup_logger()
    init_app_dirs()
    log_info('App started')
    city = ask_for_city()
    geo = geocode_city(city)
    if geo is None:
        print('City was empty, exiting')
        return
    lat, lon, name, country = geo
    data = load_cache(lat, lon)
    if data is not None:
        source = 'cache'
    else:
        data = get_forecast_24h(lat, lon)
        if data is None:
            print('Data is empty, exiting')
            return
        save_cache(lat, lon, data)
        source = 'api'
    data['meta']['name'] = name
    data['meta']['country'] = country
    data['meta']['source'] = source
    entry = {
        'timestamp': dt.now().isoformat(),
        'query': city,
        'name': name,
        'country': country,
        'lat': lat,
        'lon': lon,
        'action': 'forecast_24h',
        'source': source
    }
    append_history(entry)
    print_forecast(data)

if __name__ == '__main__':
    main()