import requests
import os
import json
from dotenv import load_dotenv
from fetch_weather import fetch_weather_data  # Import the new bulk data function

# Load environment variables
load_dotenv()

# Get Webhook URL from .env
DOMO_WEBHOOK_URL = os.getenv("DOMO_WEBHOOK_URL")

def send_bulk_weather_to_domo():
    """Fetch bulk weather data and send it to DOMO Webhook."""
    weather_data = fetch_weather_data()  # Fetch multiple cities' weather data

    if weather_data:
        headers = {"Content-Type": "application/json"}
        
        # Convert the data into JSON format
        json_data = json.dumps(weather_data)

        # Send data to DOMO
        response = requests.post(DOMO_WEBHOOK_URL, headers=headers, data=json_data)

        if response.status_code == 200:
            print(f"✅ {len(weather_data)} rows successfully sent to DOMO.")
        else:
            print(f"❌ Error sending data to DOMO: {response.status_code}, {response.text}")
    else:
        print("❌ Failed to fetch weather data.")

if __name__ == "__main__":
    send_bulk_weather_to_domo()
print("send_to_domo.py script executed successfully!")
