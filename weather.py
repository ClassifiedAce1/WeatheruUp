import requests
from config import BASE_URL, UNITS


def get_weather(city, api_key):

    url = (

            f"{BASE_URL}"

            f"?q={city}"

            f"&appid={api_key}"

            f"&units={UNITS}"

            )



    try:

        response = requests.get(url)
        data = response.json()


        if str(data.get("cod")) == "200":

            return {

                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["description"].title(),
                "wind_speed": data["wind"]["speed"]

            }

        return None

    except Exception as e:
        print(f"Error: {e}")
        return None