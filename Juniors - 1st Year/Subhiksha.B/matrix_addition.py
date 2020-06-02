r=int(input("Enter no of rows in a matrix:"))
c=int(input("Enter no of columns in a matrix:"))
A=[]
print("Enter the elements to be in the first matrix:")
for i in range(r):
   matrix1=[]
   for j in range(c):
     matrix1.append(int(input()))
   A.append(matrix1)
print(A)
B=[]
print("Enter the elements to be in the second matrix:")
for i in range(r):
   matrix2=[]
   for j in range(c):
     matrix2.append(int(input()))
   B.append(matrix2)
print(B)
C=[]
for i in range(r):
    matrix3=[]
    for j in range(c):
        matrix3.append(A[i][j]+B[i][j])
    C.append(matrix3)
print("After addition,the resultant matrix is")
print(C)


