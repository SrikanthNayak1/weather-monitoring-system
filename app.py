# app.py

import requests
import time
import json
from thresholds import check_thresholds
from db import store_daily_summary

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

API_KEY = config['api_key']
CITIES = config['cities']
INTERVAL = config['interval']

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = kelvin_to_celsius(data['main']['temp'])
        feels_like = kelvin_to_celsius(data['main']['feels_like'])
        weather_condition = data['weather'][0]['main']
        timestamp = data['dt']
        return {"city": city, "temp": temp, "feels_like": feels_like, "condition": weather_condition, "timestamp": timestamp}
    else:
        print(f"Failed to retrieve data for {city}")
        return None

def monitor_weather():
    while True:
        for city in CITIES:
            weather_data = fetch_weather_data(city)
            if weather_data:
                print(f"Weather data for {city}: {weather_data}")
                # Check for threshold violations
                alert_message = check_thresholds(weather_data['temp'], weather_data['condition'], config['thresholds'])
                if alert_message:
                    print(alert_message)
                # Store daily summaries
                store_daily_summary(weather_data)
        time.sleep(INTERVAL)

if __name__ == "__main__":
    monitor_weather()
