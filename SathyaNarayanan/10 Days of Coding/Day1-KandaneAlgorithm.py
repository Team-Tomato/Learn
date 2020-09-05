a=[1, -4, 3, 7, 2]
def mazsum(a):
    curmax=a[0];maxnow=a[0];
    for i in range(1,len(a)):
        curmax=max(a[i],curmax+a[i])
        maxnow=max(curmax,maxnow)
    return maxnow
print(mazsum(a))