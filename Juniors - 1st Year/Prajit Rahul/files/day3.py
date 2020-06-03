n=10
print("enter row and column of matrix 1")
n1=int(input())
m1=int(input())
print("enter row and column of matrix 2")
n2=int(input())
m2=int(input())
row=[]
a = [[0 for i in range(n)]  
            for j in range(n)]
b = [[0 for i in range(n)]  
            for j in range(n)]
if m1!=n2:
    print("the matrix with entered value can't be multiplied")
    exit(0)
c = [[0 for i in range(n)]  
            for j in range(n)]
print("enter matrix 1")
for i in range(n1):
    for j in range(m1):
        a[i][j]=int(input('a['+str(i)+']['+str(j)+']='))
print("enter matrix 2")
for i in range(n1):
    for j in range(m1):
        b[i][j]=int(input('b['+str(i)+']['+str(j)+']='))
print("matrix1")
for i in range(n1):
    row.append(b[i])
    for j in range(m1):
        print(a[i][j],end=' ')
    print()
print("matrix2")
for i in range(n1):
    for j in range(m1):
        print(b[i][j],end=' ')
    print()
print('ans')
for i in range(n1):
    for j in range(m2):
        for k in range(n2):
            c[i][j]+= a[i][k] * b[k][j]
for i in range(m1):
    for j in range(n1):
        print(c[i][j],end=' ')
    print()      
