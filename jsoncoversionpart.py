#2. take the required data and convert to json(key:value) format
import json
import urllib.request
from urllib.error import HTTPError, URLError
def get_weather(api_key, location):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())

                # Extract relevant information
                weather_info = {
                    'id': data['id'],
                    'city': data['name'],
                    'timeZone' : data['timezone'],
                    'weatherDescription': data['weather'][0]['description'],
                    'minTemperature': f"{data['main']['temp_min']}\u00B0C",
                    'maxTemperature': f"{data['main']['temp_max']}\u00B0C",
                    'currentHumidity': f"{data['main']['humidity']}%",
                    'windSpeed' : f"{data['wind']['speed']}m/s"
                }

            else:
                weather_info = {
                    'id' : None,
                    'name': None,
                    'timeZone' : None,
                    'weatherDescription': None,
                    'minTemperature': None,
                    'maxTemperature': None,
                    'currentHumidity': None,
                    'windSpeed' : None
                }

            return weather_info

    except HTTPError as e:
        return {'statusCode': e.code, 'error': f"HTTP Error: {e.reason}"}
    except URLError as e:
        return {'statusCode': 500, 'error': f"URL Error: {e.reason}"}
    except Exception as e:
        return {'statusCode': 500, 'error': f"Unexpected Error: {str(e)}"}

if __name__ == "__main__":
    api_key = "6869a2d6418bd4ade80e22938c9fe4d3"
    location = "London"
    output = get_weather(api_key, location)
    if output:
        json_output = json.dumps(output, indent=4 , ensure_ascii=False)
        print(json_output)

