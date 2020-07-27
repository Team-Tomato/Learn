def swap(a,b):
    a,b = b,a
    return a,b

print ("Enter the two nos to swap")
x,y=int(input()),int(input())
print("Enter any 2 characters to swap")
p,q=input(),input()
print("Swapping of numbers")
print (swap(x,y))
print("Swapping of characters")
print (swap(p,q))