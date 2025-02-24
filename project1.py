 #1. program to fetch details of weather from openweather api using api_keys(given to sir)
import json
import urllib.request
from urllib.error import HTTPError, URLError
from urllib.request import localhost


def get_weather(api_key,location):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    try:

        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                status_code = 200
                weather_description = data['weather'][0]['description'] # Capture weather
                min_temperature = data['main']['temp_min']  # Capture min temperature
                max_temperature = data['main']['temp_max']  # Capture max temperature
                current_humidity = data['main']['humidity'] # capture humidity
            else:
                status_code = response.status
                weather_description = None
                min_temperature = None
                max_temperature = None
                current_humidity= None

            return {
                'statusCode': status_code,
                'weatherDescription': weather_description,
                'minTemperature': min_temperature,
                'maxTemperature': max_temperature,
                'currentHumidity':current_humidity,
                'body': json.dumps(data) if weather_description else f"Failed to get data: {response.status}"
            }

    except HTTPError as e:
        return {
            'statusCode': e.code,
            'body': f"HTTP Error: {e.reason} (code {e.code})"
        }
    except URLError as e:
        return {
            'statusCode': 500,
            'body': f"URL Error: {e.reason}"
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Unexpected Error: {str(e)}"
        }

if __name__ == "__main__":
    api_key ="6869a2d6418bd4ade80e22938c9fe4d3"
    location ="London"

    output = get_weather(api_key,location)
    if output:
        # print(f"Status Code: {output.get('statusCode', 'No Status Code Available')}")
        # print(f"Weather in: {location}")
        # print(f"Weather Description: {output.get('weatherDescription', 'No Weather Description Available')}")
        # print(f"Minimum Temperature: {output.get('minTemperature', 'No Minimum Temperature Available')}\u00B0C")
        # print(f"Maximum Temperature: {output.get('maxTemperature', 'No Maximum Temperature Available')}\u00B0C")
        # print(f"Humidity: {output.get('currentHumidity', 'No Humidity Available')}%")
        print(output)






