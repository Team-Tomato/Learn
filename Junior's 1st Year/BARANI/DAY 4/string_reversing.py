print("***String Reversing***")
def reverse_string(string):
    index = -1
    while index >= -(len(string)):
        print(string[index],end = "")
        index -= 1
if __name__ == '__main__':
    string = input("Enter The String you wamt to reverse:")
    print("Given string :\n",string)
    print("Reversed string :")
    reverse_string(string)
    
