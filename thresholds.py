# thresholds.py

def check_thresholds(temp, condition, thresholds):
    if temp > thresholds['max_temp']:
        return f"Alert: Temperature has exceeded {thresholds['max_temp']}°C"
    if condition in thresholds['weather_conditions']:
        return f"Alert: Weather condition is {condition}"
    return None
