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

def test_places():
    city = "Hyderabad"
    key = os.getenv("PLACES_API_KEY")
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=tourist+attractions+in+{city}&key={key}"
    r = requests.get(url)
    print("Places status:", r.status_code)
    print(r.json())

test_weather()
test_places()
