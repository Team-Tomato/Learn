low = int(input("Enter the lower limit: "))
upp = int(input ("Enter the upper limit: "))
for num in range(low, upp+1):
   if num>1:
    for i in range (2, num):
      if (num%i)==0:
       break
    else:
        print(num) 
