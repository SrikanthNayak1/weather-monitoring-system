# Real-Time Weather Monitoring System

## Overview

This system retrieves real-time weather data from the OpenWeatherMap API for various cities in India. It processes the data, calculates daily aggregates, and triggers alerts based on user-defined thresholds.

## Features

- Poll weather data for specified cities at configurable intervals.
- Convert temperature from Kelvin to Celsius.
- Store daily weather summaries including average, max, and min temperatures.
- Trigger alerts if thresholds (e.g., temperature, weather condition) are breached.

## Configuration

The API key, cities, and thresholds are stored in `config.json`.

## Running the System

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-monitoring-system.git
