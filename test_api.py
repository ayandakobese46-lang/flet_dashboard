import requests

URL = "https://api.open-meteo.com/v1/forecast?latitude=-33.02&longitude=27.91&current=temperature_2m,weather_code,wind_speed_10m"

try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    data = response.json()

    current = data["current"]
    units = data["current_units"]

    print("Temperature:", current["temperature_2m"], units["temperature_2m"])
    print("Wind:", current["wind_speed_10m"], units["wind_speed_10m"])
    print("Weather code:", current["weather_code"])
except requests.exceptions.RequestException:
    print("Could not load weather. Check your connection.")