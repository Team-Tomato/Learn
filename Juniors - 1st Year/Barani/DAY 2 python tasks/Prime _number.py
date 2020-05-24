print("***PYTHON PROGRAM TO FIND PRIME NUMBER OR NOT***")
def prime(num):
    flag=0
    for i in range(2,num):
        if num%i==0:
            flag+=1
        else:
            continue
    print(num,"is a prime number") if flag==0 else print(num,"is not a Prime number")

if __name__ == "__main__" :
    num = int(input("Enter a positive integer to find a prime number or not"))
    prime(num)
