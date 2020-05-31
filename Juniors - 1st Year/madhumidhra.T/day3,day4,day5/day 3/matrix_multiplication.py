print(" multiplication of matrices")
print(" for matrix 1")
Row1 = int(input("Enter the number of rows:"))
Column1 = int(input("Enter the number of columns:"))
matrix1 = []
print("matrix 1")
print("enter the elements")
for i in range(Row1):
    a = []
    for j in range(Column1):
        j=int(input())
        a.append(j)
    matrix1.append(a)
for i in range(Row1):
    for j in range(Column1):
        print(matrix1[i][j], end = " ")
    print()

print(" for matrix 2")
Row2 = int(input("Enter the number of rows:"))
Column2 = int(input("Enter the number of columns:"))
matrix2= []
print("matrix 2")
print("enter the elements")
for i in range(Row2):
    b = []
    for j in range(Column2):
        j=int(input())
        b.append(j)
    matrix2.append(b)
for i in range(Row2):
    for j in range(Column2):
        print(matrix2[i][j], end = " ")
    print()
print(" the multiplication of 2 matrices is ")
print()
C=[[0 for i in range (Row1)]
    for j in range (Column2)]
for i in range(Row1):
    for j in range(Column2):
        C[i][j]=0
        for k in range(Column1):
                C[i][j]+=matrix1[i][k]*matrix2[k][j]

print(C)

