print(" addition of matrices")
print(" for matrix 1")
Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))
matrix1 = []
print("matrix 1")
print("enter the elements")
for i in range(Row):
    a = []
    for j in range(Column):
        j=int(input())
        a.append(j)
    matrix1.append(a)
for i in range(Row):
    for j in range(Column):
        print(matrix1[i][j], end = " ")
    print()

print(" for matrix 2")
Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))
matrix2= []
print("matrix 2")
print("enter the elements")
for i in range(Row):
    b = []
    for j in range(Column):
        j=int(input())
        b.append(j)
    matrix2.append(b)
for i in range(Row):
    for j in range(Column):
        print(matrix2[i][j], end = " ")
    print()
print(" the addition of 2 matrices is ")
print()
matrix3=[]
for i in range(Row):
    c = []
    for j in range(Column):
        add = matrix1[i][j] + matrix2[i][j]
        c.append(add)
    matrix3.append(c)
for i in range(Row):
    for j in range(Column):
        print(matrix3[i][j],end=" ")
    print()