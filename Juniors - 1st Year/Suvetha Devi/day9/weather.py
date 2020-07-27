import requests,json

def weather_predict(city):
       api_key = "8ad3142f0047f24ecacce4076f003ddc"
       Base_url = "https://api.openweathermap.org/data/2.5/weather?"
       url = Base_url  +"&appid=" + api_key + "&q=" + city
       response = requests.get(url)
       if response.status_code==200:
            data=response.json()
            main=data['main']
            temperature=round(main['temp']-273,1)
            humidity=main['humidity']
            pressure=main['pressure']
            report=data['weather']
            print(f"{city:-^30}")
            print(f"Temperature:{temperature}")
            print(f"Humidity:{humidity}")
            print(f"Pressure:{pressure}")
            print(f"Weather report:{report[0]['description']}")
       else:
          print("Error in HTTP request")
repeat='r'
if repeat=='r':
        x = input("Enter the name of the city to predict the weather")
        weather_predict(x)
        repeat=input("Enter 'r' to repeat the process")
