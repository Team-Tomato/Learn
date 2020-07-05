n=int(input())
a = [[0 for i in range(n)]  
            for j in range(n)]
b = [[0 for i in range(n)]  
            for j in range(n)]
print("enter matrix 1")
for i in range(n):
    for j in range(n):
        a[i][j]=int(input())
print("enter matrix 2")
for i in range(n):
    for j in range(n):
        b[i][j]=int(input())
for i in range(n):
    for j in range(n):
        print(a[i][j] + b[i][j],end=" ")
    print()
