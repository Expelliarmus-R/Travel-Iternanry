import requests, os
from dotenv import load_dotenv
load_dotenv()

def test_weather():
    city = "Hyderabad"
    key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    r = requests.get(url)
    print("Weather status:", r.status_code)
    print(r.json())



test_weather()

