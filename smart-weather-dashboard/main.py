from src.weatherChecker import WeatherDashboard, WeatherProvider
import json

print('===============================')
print('         SMART-WEATHER')
print('===============================')

input_user = input("Enter the city name: ")

app = WeatherDashboard(input_user)
app.run()