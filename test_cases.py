# test_cases.py

from app import kelvin_to_celsius, fetch_weather_data

def test_kelvin_to_celsius():
    assert kelvin_to_celsius(300) == 26.85, "Temperature conversion failed"

def test_fetch_weather_data():
    weather_data = fetch_weather_data("Delhi")
    assert weather_data is not None, "Failed to fetch weather data"
    assert "temp" in weather_data, "Temperature not found in weather data"

if __name__ == "__main__":
    test_kelvin_to_celsius()
    test_fetch_weather_data()
    print("All tests passed.")
