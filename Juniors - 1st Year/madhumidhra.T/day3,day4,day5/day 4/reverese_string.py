print(" a python code to reverse a string manually")
def reverse(a):
    reversed_string =" "
    for i in a:
        reversed_string=i+reversed_string
    print("the reversed string is",reversed_string)
a=str(input("enter the  string"))
print(" entered string",a)
reverse(a)
print()
print(" using python functions")
b=str(input("enter the  string"))
reversed_string="" .join(reversed(b))
print("the reversed string is",reversed_string)