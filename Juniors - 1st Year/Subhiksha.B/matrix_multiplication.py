r1=int(input("Enter no of rows in  first matrix:"))
c1=int(input("Enter no of columns in first matrix:"))
r2=int(input("Enter no of rows in second matrix:"))
c2=int(input("Enter no of columns in second matrix:"))
if c1 != r2:
    print("For multiplication,c1 and r2 should be equal,Re-enter your values\n")
else:
    A=[]
    print("Enter the elements to be in the first matrix:")
    for i in range(r1):
        matrix1=[]
        for j in range(c1):
             matrix1.append(int(input()))
        A.append(matrix1)
    print(A)
    B=[]
    print("Enter the elements to be in the second matrix:")
    for i in range(r2):
        matrix2=[]
        for j in range(c2):
            matrix2.append(int(input()))
        B.append(matrix2)
    print(B)
    C=[]
   #C=[ [0 for i in range(r1)]
          # for j in range(c2)]
    for i in range(r1):
        matrix3 = []
        for j in range(c2):
            sum = 0
            for k in range(c1):
                sum += A[i][k] * B[k][j]
            matrix3.append(sum)
        C.append(matrix3)
    print("After multiplication, the resultant matrix ")
    print(C)