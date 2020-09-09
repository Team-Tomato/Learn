from math import *
def rectangle():
    l=int(input("Enter the length"))
    b=int(input("Enter the breadth"))
    A=l*b
    print("The area of the rectangle is ",A)
    menu()

def triangle():
    b=int(input("Enter the value of base"))
    h=int(input("Enter the value of height"))
    A=0.5*b*h
    menu()

def circle():
    r=int(input("Enter the value of radius"))
    A=3.14*sqrt(r)
    menu()

def menu():
    print("Enter the option which you want to calculate")
    print("1.Area of rectangle")
    print("2.Area of rectangle")
    print("3.Area of rectangle")
    print("4.Quit")
    ch=int(input())
    return ch


s=menu()
while(s<4):
 if(s==1):
  rectangle()
 elif(s==2):
  triangle()
 elif(s==3):
  circle()
 else:
     print("Choose from the given options")
s=menu()




