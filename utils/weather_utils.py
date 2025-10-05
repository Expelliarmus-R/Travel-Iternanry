import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        return None

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "city": data.get("name"),
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"],
        }
    return None
