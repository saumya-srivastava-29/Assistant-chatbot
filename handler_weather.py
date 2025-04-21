import requests
import spacy
from nlp_utils import get_nlp


def extract_city(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "GPE":
            return ent.text

    # Fallback: if user just types a city (like 'Rome'), trust it
    cleaned = text.strip()
    if len(cleaned.split()) == 1:  # Single word input? Assume it's a city
        return cleaned.title()

    return None



def handle_get_weather(user_input):
    city = extract_city(user_input)

    if not city:
        return "🌦️ Please mention the city you'd like the weather for."

    if city.lower() in ["weather", "forecast", "temperature"]:
        return "🌦️ Please mention the city you'd like the weather for."



    # Build and send API request
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=d0e32e530ec4d79a1d22f622f8fb8787&units=metric"
    print("DEBUG — Extracted city:", city)
    print("DEBUG — API URL:", url)

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            return f"❌ Couldn’t find weather for '{city}'. Please check the spelling."

        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]

        return f"🌤️ Weather in {city.title()}: {weather_desc}, {temp}°C."

    except Exception as e:
        return f"⚠️ Error fetching weather: {str(e)}"
