print(" a program to predict the current weather")
celsius=float(input("enter the degree in celcius"))
fahrenheit=((celsius*1.8)+32)
print("celsius:",celsius)
print("fahrenheit:",fahrenheit)
if(celsius<0):
    print("icy freeze cold")
elif(celsius<=10):
        print("cold weather")
elif(celsius<=22):
        print("cool weather")
elif(celsius<=35):
        print("light cloud and gentle breeze  cloudy weather")
elif(celsius<=37):
        print("sunny intervals and an gentle breeze weather")
elif(celsius>41):
        print("hot weather")


