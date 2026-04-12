import requests
import os

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
def simplify_weather(condition):
    condition = condition.lower()

    if "rain" in condition or "drizzle" in condition or "thunderstorm" in condition:
        return "Raining"
    elif "cloud" in condition:
        return "Cloudy"
    elif "clear" in condition:
        return "Sunny"
    elif "haze" in condition or "fog" in condition or "mist" in condition:
        return "Foggy"
    elif "snow" in condition:
        return "Snowy"
    else:
        return condition.title()

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        temp = data["main"]["temp"]
        condition_raw = data["weather"][0]["description"]

        condition = simplify_weather(condition_raw)

        return temp, condition

    except:
        return None, None
def will_rain_next_12_hours(city):
    url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "cnt": 4
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        for item in data["list"]:
            if item["weather"][0]["id"] < 700:
                return True

        return False
    except:
        return None