n=int(input())
count=0
if n>1 and n!=4 :
    for i in range(2,int(n/2)):
        if n%i==0:
            count+=1
            break
if(n==4 or count==1):
    print("not a prime")
else:
    print("prime")
