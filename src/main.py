from weather import fetch_weather


if __name__ == "__main__":
    # This block will only run if the script is executed directly
    city = input("Enter a city name: ")
    weather_info = fetch_weather(city)
    print(weather_info)

    