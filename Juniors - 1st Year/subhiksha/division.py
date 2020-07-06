print("Enter divisor and divider:")
x=int(input("x:"))
y=int(input("y:"))
if y==0:
  print("Re-enter your divider value which is not equal to 0")
else:
  quotient=x//y
  remainder=x%y
print("Quotient=",quotient)
print("Remainder=",remainder)