print("***PRIME NUMBER PROGRAM***")
num=int(input("Enter positive integer to find prime number or not\n"))
for i in range(2,num//2):
    if num%i == 0:
        print(num," is a prime number")
        break
else:    
    print(num," is not a prime number")