# Real-Time Weather Monitoring System

## Overview

This system retrieves real-time weather data from the OpenWeatherMap API for various cities in India. It processes the data, calculates daily aggregates, and triggers alerts based on user-defined thresholds.

### Features:
- Poll weather data for specified cities at configurable intervals.
- Convert temperature from Kelvin to Celsius.
- Store daily weather summaries, including average, max, and min temperatures.
- Trigger alerts if thresholds (e.g., temperature exceeding 35°C or rainy conditions) are breached.
- Visualize historical weather trends and alerts.

### Data Source:
The system uses data from the OpenWeatherMap API to track the following weather parameters:
- `main`: Main weather condition (e.g., Rain, Snow, Clear).
- `temp`: Current temperature in Celsius.
- `feels_like`: Perceived temperature in Celsius.
- `dt`: Timestamp of the data update.

## System Components

1. **Weather Data Polling:**
   - Polls weather data every 5 minutes (configurable).
   - Retrieves and parses the weather data from the OpenWeatherMap API for cities like Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.

2. **Temperature Conversion:**
   - Converts temperature from Kelvin to Celsius using a simple conversion formula.

3. **Daily Weather Summaries:**
   - The system aggregates weather data into daily summaries, including the average, minimum, and maximum temperatures, as well as the dominant weather condition of the day.

4. **Alerting System:**
   - Alerts are triggered if the temperature exceeds 35°C or if a specific weather condition, such as Rain, is detected.

5. **Data Storage:**
   - The system stores daily weather summaries for future reference and analysis.

## Dashboard Visualization

The system dashboard provides a visual summary of real-time weather data, historical trends, and triggered alerts. Below is an example of the system's user interface, which displays data for multiple cities, along with notifications when thresholds are breached.

![Weather Monitoring System Interface](./mnt/data/A_real-time_weather_monitoring_system_interface_th.png)

## Configuration

The API key, cities to monitor, and alert thresholds are stored in the `config.json` file. Here's an example:

```json
{
    "api_key": "your_openweathermap_api_key",
    "interval": 300,
    "cities": ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"],
    "thresholds": {
        "max_temp": 35,
        "weather_conditions": ["Rain", "Snow"]
    }
}
