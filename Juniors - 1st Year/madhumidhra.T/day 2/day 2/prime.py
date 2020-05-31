num=int(input("enter the number"))

if (num > 1):
    for i in range (2, num//2):
        if ((num % i) == 0):
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "it is an negative number, since prime cannot be found")