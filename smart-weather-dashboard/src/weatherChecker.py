import requests

class WeatherProvider:
    def __init__(self, API:str):
        self.api = API
        self.url = "https://api.openweathermap.org/data/2.5/weather"

    def fetch_data(self, city:str):
        params = {
            "q" : city,
            "appid" : self.api,
            "units" : "metric",
            "lang" : "en"
        }

        response = requests.get(self.url, params)
        response.raise_for_status()

        return response.json()


class WeatherDashboard:
    def __init__(self, city: str, key="75362e63c015a77c4d79c585a4e7001a"):
        self.city = city
        self.provider = WeatherProvider(key)

    def run(self):
        try:
            data = self.provider.fetch_data(self.city)

            print(f'\nCurrent Weather Report:')
            print(f'- City : {data['name']}')
            print(f'- Temperature : {data['main']['temp']}°C')
            print(f'- Conditions: {data['weather'][1]['description']}')

        except Exception as e:
            print(f'Error : {e}')