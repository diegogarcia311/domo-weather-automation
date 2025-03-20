import requests
import os
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# API endpoint
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# List of solar-relevant cities
CITIES = [
    "Phoenix,US", "Las Vegas,US", "Los Angeles,US", "San Diego,US",
    "Denver,US", "Austin,US", "Miami,US", "New York,US",
    "San Francisco,US", "Salt Lake City,US"
]

def fetch_weather_data():
    """Fetch weather data for multiple cities."""
    all_weather_data = []
    
    for city in CITIES:
        try:
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"  # Use "imperial" for Fahrenheit
            }
            
            response = requests.get(BASE_URL, params=params)

            if response.status_code == 200:
                data = response.json()
                weather_entry = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "feels_like": data["main"]["feels_like"],
                    "temp_min": data["main"]["temp_min"],
                    "temp_max": data["main"]["temp_max"],
                    "humidity": data["main"]["humidity"],
                    "pressure": data["main"]["pressure"],
                    "visibility": data.get("visibility", "N/A"),
                    "weather": data["weather"][0]["description"],
                    "wind_speed": data["wind"]["speed"],
                    "wind_direction": data["wind"]["deg"],
                    "sunrise": data["sys"]["sunrise"],
                    "sunset": data["sys"]["sunset"]
                }
                all_weather_data.append(weather_entry)
                print(f"✅ Data fetched for {city}")
            else:
                print(f"❌ Failed to fetch data for {city}: {response.status_code} - {response.json()['message']}")
        
        except Exception as e:
            print(f"⚠ Error processing {city}: {str(e)}")

        time.sleep(1)  # Avoid API rate limits

    return all_weather_data

if __name__ == "__main__":
    weather_data = fetch_weather_data()
    print(weather_data)
