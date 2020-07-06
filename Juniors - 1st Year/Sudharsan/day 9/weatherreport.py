import requests
city=input("Enter the city name")
url="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=487e2d88904b38cc208e857d8bb200ea"
data=requests.get(url)
read=data.json()
print("City name :{}".format(read['name']))
print("Temaperature :{}F".format(read['main']['temp']))
print("Description :{}".format(read['weather'][0]['description']))
