from rich.console import Console
## Convert user input
console = Console()
def ask_for_city():
    raw_input = input('Enter city: ')
    city = raw_input.strip()
    if city != '':
        return city
    else:
        console.print('City cannot be empty! :cross_mark:', style='bold underline red')
        return

def print_forecast(data):
    meta = data['meta']
    items = data['items']
    city = meta['name']
    console.print(f'Weather forecast - next 24 hours', style='bold underline yellow')
    console.print(f'City: {city}', style='bold underline yellow')
    console.print(f'Source: Openweather', style='bold underline yellow')
    console.print(f'------------------', style='bold white')
    for item in items:
        time = item['dt_txt']
        temp = item['main']['temp']
        desc = item['weather'][0]['description']
        wind = item['wind']['speed']
        console.print(f'{time} {temp} {desc} {wind}', style='bold underline green')