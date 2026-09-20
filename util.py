def display_weather(city, weather_data):

    print("\n----- Weather Report -----")

    print(f"City: {city.title()}")

    print(f"Temperature: {weather_data['temp']}°C")

    print(f"Humidity: {weather_data['humidity']}%")

    print(f"Condition: {weather_data['condition']}")

    print(f"Wind Speed: {weather_data['wind_speed']} m/s")

    print("--------------------------")