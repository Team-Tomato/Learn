import requests , json
#d65addd11459746684d25f814665cedb
def get_weather():
    API_key = input("Enter your API key to fetch current weather of a city:")
    base_url =  "http://api.openweathermap.org/data/2.5/weather?"
    city_name = input("Enter city name to fetch current weather:")
    URL = base_url+"appid="+API_key+"&q="+city_name
    response1 = requests.get(URL)
    response = response1.json()
    if response["cod"] != "404":
        y = response["main"]
        temperature = y["temp"]
        pressure = y["pressure"]
        humidity = y["humidity"]
        maximum_temperature = y["temp_max"]
        minimum_temperature = y["temp_min"]
        w = response["weather"]
        description = w[0]["description"]
        print("\nTemperature of the city:",temperature)
        print("\nPressure of the city:",pressure)
        print("\nHumidity of the city:",humidity)
        print("\nmaximum_temperature of the city:",maximum_temperature)
        print("\nminimum_temperature of the city:",minimum_temperature)
        print("\nWeather description of the city:",description)
    else:
        print("City is not found")
if __name__ =='__main__':
    ch = input("Enter any alphabet except q to know the weather of the city:")
    while ch!="q":
        get_weather()
        ch =input("Enter q to quit or enter any alphabet to continue:")
print("You entered q to quit")
