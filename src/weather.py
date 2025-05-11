import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BASE_WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("OPENWEATHER_API_KEY")


#api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial"

def get_lat_lon(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "imperial"
    }
    
    #api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"

    try:
        response = requests.get(BASE_WEATHER_API_URL,params=params,timeout=5)
        data = response.json()
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]

        return lat, lon
    except requests.exceptions.RequestException as e:
        print(f"Error fetching coordinates: {e}")
        return None, None

def fetch_weather(city):

    lat, lon = get_lat_lon(city)

    if lat is not None and lon is not None:
        #api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial"
        
        params = {
            "lat": lat,
            "lon": lon,
            "appid": API_KEY,
            "units": "imperial"
        }

        response = requests.get(BASE_WEATHER_API_URL, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()

            return (
                f"The current temperature in {data['name']} is {data['main']['temp']}°F \n"
                F"It feels like {data['main']['feels_like']}°F and \n"
                F"The weather outside is {data['weather'][0]['description']} and wind speed is {data['wind']['speed']} miles/hr.\n")
        else:
            return f"Error: {response.status_code}"
    else:
            return "Error: City Not found"