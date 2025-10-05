import streamlit as st
from agent import run_agent
from utils.weather_utils import get_weather
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_KEY = os.getenv("WEATHER_API_KEY")

print("Weather Key:", WEATHER_KEY)  # DEBUG

# 🔹 MUST BE FIRST
st.set_page_config(page_title="🌍 AI Travel Planner", page_icon="✈️")

st.title("🌍 AI Travel Planner")

# User Input
destination = st.text_input("Enter your destination:")
days = st.number_input("Number of days", min_value=1, max_value=30, value=3)

if st.button("Generate Plan"):
    if destination.strip():
        with st.spinner("Generating AI itinerary..."):
            itinerary_prompt = (
                f"Create a detailed {days}-day travel itinerary for {destination}. "
                f"Include best activities, food recommendations, and travel tips."
            )
            itinerary = run_agent(itinerary_prompt)

        st.subheader("📌 Travel Itinerary")
        st.write(itinerary)

        st.subheader("🌤 Current Weather")
        weather = get_weather(destination)
        if weather:
            st.write(f"{weather['temp']}°C, {weather['description'].title()}")
        else:
            st.error("Weather data not available.")
    else:
        st.warning("Please enter a destination to continue.")
#### will add somemore