

def prime(x):
    flag = 0
    for i in range(2,x):
        if x%i==0:
            flag+=1
        else:
            continue
    if flag==0:
        print(x,"is a prime number")
    else:
        print(x ,"is not a prime number")
num=int(input("Enter a number to find whether it is a prime number or not"))
prime(num)