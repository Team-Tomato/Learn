

def deci_to_bin(num):
    if num>1:
        deci_to_bin(num//2)
    print(num%2, end=" ")

dec = int(input("Enter positive decimal number to convert into binary"))
deci_to_bin(dec)