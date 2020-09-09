print("Enter divident and divisor:")
x=int(input("x:"))
y=int(input("y:"))
if y==0:
  print("Re-enter your divisor value which is not equal to 0")
else:
  quotient=x//y
  remainder=x%y
print("Quotient=",quotient)
print("Remainder=",remainder)