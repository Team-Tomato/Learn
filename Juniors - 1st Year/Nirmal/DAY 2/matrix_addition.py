row=int(input("Enter the rows for matirx_1and matrix_2: "))
col=int(input ("Enter the columns for matrix_1 and matrix_2: "))
print("Enter the elements for matrix_1: ")
matrix_1 =[ [int(input()) for i in range(col)] for j in range(row)]
print("matrix_1 is: ")
for i in range(row):
      for j in range(col):
            print(format(matrix_1[i] [j], "<5"), end=" ")
      print()
print("Enter the elements for matrix_2: ")
matrix_2 =[ [int(input()) for i in range(col)] for j in range (row) ]
print("matrix_2 is: ")
for i in range(row):
      for j in range(col):
            print(format(matrix_2 [i] [j], "<5"), end=" ")
      print()
result = [ [ 0 for i in range(col)] for j in range(row) ]
for i in range(row):
       for j in range(col):
             result [i] [j] = matrix_1 [i] [j]  + matrix_2 [i] [j]
                   
print("Result is: ")
for i in range(row):
      for j in range (col):
            print(format(result [i] [j], "<5"), end=" ")
      print()
