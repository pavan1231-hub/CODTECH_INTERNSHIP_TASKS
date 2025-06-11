import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

API_KEY = "6ae7da11887ccc1ab23c36438cf1263e" # Replace with your actual API key
CITY = "chittoor" #select your wish 
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

# Fetching weather data
def fetch_weather_data(city, api_key):
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Processing data
def process_weather_data(data):
    dates = []
    temps = []
    for entry in data["list"]:
        timestamp = entry["dt"]
        date = datetime.datetime.fromtimestamp(timestamp)
        temp = entry["main"]["temp"]
        dates.append(date)
        temps.append(temp)
    return dates, temps

# Visualizing data
def visualize_weather(dates, temps):
    sns.set(style="whitegrid")
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=dates, y=temps, marker="o", color="b")
    plt.title(f"Weather Forecast for {CITY}", fontsize=16)
    plt.xlabel("Date and Time", fontsize=12)
    plt.ylabel("Temperature (°C)", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main execution
if __name__ == "__main__":
    weather_data = fetch_weather_data(CITY, API_KEY)
    if weather_data:
        dates, temps = process_weather_data(weather_data)
        visualize_weather(dates, temps)
