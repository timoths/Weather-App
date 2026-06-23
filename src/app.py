import requests

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPEN_WEATHER_API")

user_state = input("Enter State: ")

user_city = input("Enter City: ")

location_data = requests.get(
    f"http://api.openweathermap.org/geo/1.0/direct?q={user_city},{user_state},USA&limit=1&appid={api_key}"
)

lon = location_data.json()[0]['lon']
lat = location_data.json()[0]['lat']

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={api_key}")


weather = weather_data.json()['weather'][0]['main']

temp = weather_data.json()['main']['temp']

print(f"Weather in {user_city.capitalize()}: {weather}, Temperature: {temp}")