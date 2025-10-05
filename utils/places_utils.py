import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_places(city):
    api_key = os.getenv("PLACES_API_KEY")
    if not api_key:
        return None

    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=tourist+attractions+in+{city}&key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])
        return [place["name"] for place in results[:5]]
    return None
