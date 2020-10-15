def divide(divnd,divisor):
    quo = divnd/divisor
    rem = divnd%divisor
    return quo,rem

x = int(input("Enter the dividend"))
y= int(input("Enter the divisor"))
print (divide(x,y))