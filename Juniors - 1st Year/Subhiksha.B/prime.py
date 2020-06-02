number=int(input("Enter the number to be checked prime or not:"))
if  number == 1:
  print("1 is  neither  a  composite nor  prime   number")
else:
  count=0
  for i in range(2,number//2):
    if number % i == 0:
       count = count + 1
  if count == 0:
    print("Given number is  a prime number")
  else:  
    print("Given number is not a  prime number")