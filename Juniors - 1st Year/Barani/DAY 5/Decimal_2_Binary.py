print("***CONVERTING DECIMAL TO BINARY***")
def Decimal_2_binary(dec):
    if dec > 1:
        Decimal_2_binary(dec//2)
    print(dec%2, end = '')

if __name__ == '__main__':
    ch = 'r'
    while ch == 'r':
        dec = int(input("Enter positive Decimal number needs to be conerted to binary: "))
        print("Binary value for Decimal number %d : ",dec)
        Decimal_2_binary(dec)
        ch = str(input("\nEnter \'r\' to repeat the prcess: "))