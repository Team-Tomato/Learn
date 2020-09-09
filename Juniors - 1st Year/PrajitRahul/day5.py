n=int(input())
a=[]
i=0
while(int(n)>0):
    a.append(int(n%2))
    n/=2
    i+=1
f="".join(str(a.pop()) for j in range(i,0,-1))
print(f)
