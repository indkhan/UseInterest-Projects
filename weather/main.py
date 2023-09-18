import apikey
import requests
api = apikey.api_key

def weatherreport(city):

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    request_url = f"{base_url}?appid={api}&q={city}"
    response = requests.get(request_url)
    data = response.json()
    weather = data["weather"][0]["description"]
    temp = int(data["main"]["temp"]) - 273.15
    feel = int(data["main"]["feels_like"]) - 273.15
    humidity = data["main"]["humidity"]


    return(f"the weather in {city} is {weather} ,the temperature is {round(temp,2)}'C but feels like {round(feel,2)}'C and the humidity is {humidity}%")


if __name__ == "__main__":
    city = input("enter the city name: ")
    print(weatherreport(city))