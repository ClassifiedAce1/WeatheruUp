def display_weather(city, weather_data):
2
print("\n----- Weather Report -----")
3
print(f"City: {city.title()}")
4
print(f"Temperature: {weather_data['temp']}°C")
5
print(f"Humidity: {weather_data['humidity']}%")
6
print(f"Condition: {weather_data['condition']}")
7
print(f"Wind Speed: {weather_data['wind_speed']} m/s")
8
print("--------------------------")