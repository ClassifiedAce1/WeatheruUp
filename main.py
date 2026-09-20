from weather import get_weather
from config import API_KEY

def main():
    city = input("Enter city: ")
    data = get_weather(city, API_KEY)
    if data:
        print(f"City: {city}")
        print(f"Temperature: {data['temp']}°C")
        print(f"Humidity: {data['humidity']}%")
        print(f"Condition: {data['condition']}")
    else:
        print("City not found.")

if __name__ == "__main__":
    main()