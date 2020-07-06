def reverse(s) :
    str = " "
    for i in s :
        str = i + str
    print("Reversed name is: ", str)
s =input("Enter a name: ")
print("original name is: ", s)
reverse(s) 
