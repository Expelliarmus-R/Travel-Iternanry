import os
from dotenv import load_dotenv

load_dotenv()
print("Weather Key:", os.getenv("WEATHER_API_KEY"))
print("Places Key:", os.getenv("PLACES_API_KEY"))
