import os

import requests


def get_weather() -> None:
    API_KEY = os.getenv("API_KEY")
    if not API_KEY:
        print("API KEY not found. Set environment variable.")
        return
    URL = "http://api.weatherapi.com/v1/current.json"
    FILTERING = "Paris"
    params = {
        "key": API_KEY,
        "q": FILTERING
    }
    print(f"Performing request to Weather API for city {FILTERING}...")
    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        data = response.json()
        location = data["location"]["name"]
        country = data["location"]["country"]
        time = data["current"]["last_updated"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"{location}/{country} {time} Weather: {temperature} Celsius, {condition}")
    except requests.RequestException as e:
        print("Error while getting weather data:", e)

if __name__ == "__main__":
    get_weather()
