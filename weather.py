import requests
2
from config import BASE_URL, UNITS
3
 
4
 
5
def get_weather(city, api_key):
6
url = (
7
f"{BASE_URL}"
8
f"?q={city}"
9
f"&appid={api_key}"
10
f"&units={UNITS}"
11
)
12
 
13
try:
14
response = requests.get(url)
15
data = response.json()
16
 
17
if str(data.get("cod")) == "200":
18
return {
19
"temp": data["main"]["temp"],
20
"humidity": data["main"]["humidity"],
21
"condition": data["weather"][0]["description"].title(),
22
"wind_speed": data["wind"]["speed"]
23
}
24
 
25
return None
26
 
27
except Exception as e:
28
print(f"Error: {e}")
29
return None