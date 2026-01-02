from src.weatherChecker import WeatherDashboard
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

print('===============================')
print('         SMART-WEATHER')
print('===============================')

input_user = input("Enter the city name: ")

app = WeatherDashboard(input_user, api_key)
app.run()