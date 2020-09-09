p1=int(input("Enter the rows for matirx_1: "))
q1=int(input ("Enter the columns for matrix_1: "))
print("Enter the elements for matrix_1: ")
matrix_1 =[ [int(input()) for i in range(p1)] for j in range(q1)]
print("matrix_1 is: ")
for i in range(p1):
      for j in range(q1):
            print(format(matrix_1[i] [j], "<5"), end=" ")
      print()
      
print("Enter the elements for matrix_2: ")
p2=int(input("Enter the rows for matirx_2: "))
q2=int(input ("Enter the columns for matrix_2: "))
matrix_2 =[ [int(input()) for i in range(p2)] for j in range (q2) ]
print("matrix_2 is: ")
for i in range(p2):
      for j in range(q2):
            print(format(matrix_2 [i] [j], "<5"), end=" ")
      print()
      
if(q1 == p2):
      result = [ [ 0 for i in range(q1)] for j in range(p2) ]
      for i in range(p1):
            for j in range(q2):
                  for k in range(p2):
                   result [i] [j] = result [i] [j] + matrix_1 [i] [k]  *  matrix_2 [k] [j]           
      print("Result is: ")
      for i in range(q1):
            for j in range (p2):
                  print(format(result [i] [j], "<5"), end=" ")
            print()
else:
        print("Cannot perform matix multiplication.")
