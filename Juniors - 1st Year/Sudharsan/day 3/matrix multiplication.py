from numpy import *
r1=int(input("Enter the no of rows in matrix 1"))
c1=int(input("Enter the no of coloums in matrix 1"))

r2=int(input("Enter the no of rows in matrix 2"))
c2=int(input("Enter the no of coloums in matrix 2"))
print("Enter the elements in matrix 1")
matrix1=[]
for i in range(r1):
    a=[]
    for j in range(c1):
        a.append(int(input()))
    matrix1.append(a)

print("Enter the elements in matrix 2")
matrix2=[]
for i in range(r2):
    b=[]
    for j in range(c2):
        b.append(int(input()))
    matrix2.append(b)

result=matrix('0 0; 0 0')
print(result)
if r1==c2:
  matrix3=[]
  for i in range(r1):
      for j in range(c2):
          for k in range(c1):
              result[i][j]+=matrix1[i][k]*matrix2[k][j]


for i in range(r1):
    for j in range(c2):
          print(matrix3[i][j], end=" ")
    print()

else:
    print("We cant perform matrix multiplication")



