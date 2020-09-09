a = list(map(int,input().split()))
me = ms = a[0]
for i in range(1,len(a)):
    me += a[i]
    if me < a[i]:
        me = a[i]
    if ms < me:
        ms = me
print(ms)
