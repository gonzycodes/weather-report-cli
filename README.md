# Weather CLI
This CLI program fetches weather data for an optional city.
It uses an external weather API, saves history and cached data locally, and logs program events.
The purpose of the project is to showcase clear project structure, an isolated environment and version control.

## Features
- Fetch 24h weather data from a specified city
- Display a weather forecast
- Save and display previous searches (history)
- Use local caching to minimize API calls
- Structured logging using Loguru

## Requirements
- Python 3.10+
- OpenWeather API key (free tier)

# Installation
## Clone repository
git clone https://github.com/YOUR_USERNAME/weather-report-cli.git
cd weather-report-report-cli
## Create and activate venv
python -m venv .venv
source .venv/bin/activate - (May wary depending on OS)
## Dependencies
pip install -r requirements.txt

# API Key Setup
Create free api at openweather.org
Add your api in
module: src/weather/config.py
line: OPENWEATHER_API_KEY = '...'

# Running the application
From project root do:
cd src
python -m app

## File structure
```plaintext
weather-report-cli/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── __main__.py      
│   │   └── cli.py          
│   │
│   ├── weather/
│   │   ├── __init__.py
│   │   ├── config.py        
│   │   ├── logger.py        
│   │   ├── client.py        
│   │   └── storage.py       
│   │
│   └── data/                
│       ├── cache/
│       └── history.json
│
├── logs/                    
│   └── app.log
│
└── .venv/                   
```

