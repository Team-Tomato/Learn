import requests, json

def get_weather(city):
    api_key = "8ad3142f0047f24ecacce4076f003ddc"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    x = requests.get(complete_url) 
    response = x.json()

    if response["cod"] != "404": 
        main = response["main"] 
        temperature = round(main["temp"]-273,1) 
        humidiy = main["humidity"]
        weather = response["weather"] 
        weather_description = weather[0]["description"] 

        print(" Current Temperature = " + str(temperature) + " C" +
              "\n Weather description = " + str(weather_description) + 
              "\n Humidity = " + str(humidiy) + " %")
    else: 
        print(" City Not Found ")

if __name__ == '__main__':
    ch = 'r'
    while ch == 'r':
        city = str(input("Enter city name : "))
        get_weather(city)
        ch = input("Enter \'r\' to repeat the process: ")
    print("EXIT")
