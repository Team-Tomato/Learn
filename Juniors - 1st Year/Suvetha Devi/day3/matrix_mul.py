
arr1 = []
arr2 = []
n = int(input("Enter n for n*n matrix"))
print("Enter the element")
for i in range(n):
    row=[]
    for j in range(n):
              row.append(int(input()))
    arr1.append(row)
print(arr1)
print("array in matrix format")
for i in range(n):
    for j in range(n):
        print(arr1[i][j],end=" ")
    print()
n = int (input("Enter n for n*n matrix"))
print("Enter the element")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    arr2.append(row)
print(arr2)
print("array in matrix format")
for i in range(n):
    for j in range(n):
        print(arr2[i][j],end=" ")
    print()
res = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(n):
    for j in range(len(arr1[0])):
        for k in range(len(arr1)):
                res[i][j] += arr1[i][k] * arr2[k][j]

for r in res:
    print("Resultant matrix",r)

