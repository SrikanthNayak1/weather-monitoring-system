# db.py

import json

def store_daily_summary(weather_data):
    # Simulate storing data in a file (could use database instead)
    with open("daily_summaries.json", "a") as f:
        f.write(json.dumps(weather_data) + "\n")
    print(f"Stored summary for {weather_data['city']} at {weather_data['timestamp']}")
