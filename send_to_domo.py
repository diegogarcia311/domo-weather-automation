import requests
import os
import json

# Load environment variables
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
DOMO_WEBHOOK_URL = os.getenv('DOMO_WEBHOOK_URL')

# Example function to fetch weather data
def fetch_weather(city="Phoenix,US"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch weather data: {response.status_code}")
        return None

# Send data to DOMO Webhook
def send_to_domo():
    weather_data = fetch_weather()
    if weather_data:
        formatted_data = {
            "city": weather_data["name"],
            "temperature": weather_data["main"]["temp"],
            "humidity": weather_data["main"]["humidity"],
            "weather": weather_data["weather"][0]["description"]
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(DOMO_WEBHOOK_URL, headers=headers, data=json.dumps([formatted_data]))
        print(f"Data sent to DOMO: {response.status_code}")

if __name__ == "__main__":
    send_to_domo()
