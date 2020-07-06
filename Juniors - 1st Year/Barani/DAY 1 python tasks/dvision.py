print("***Python program to divide 2 numbers and get the quotient and remainder***")
def divide(num1,num2):
    print("Quotient for dividing", num1,"by",num2," = ",num1/num2)
    print("remainder for dividing", num1,"by",num2," = ",num1%num2)
if __name__ == '__main__':
    num1 = int(input("Enter divident = "))
    num2 = int(input("Enter divisor = "))
    divide(num1,num2)