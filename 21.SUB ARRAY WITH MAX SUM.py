n=int(input())
l=list(map(int,input().split()))
s=l[0]
ms=l[0]
for i in range(1,n):
    s=max(l[i],s+l[i])
    ms=max(ms,s)
print(ms)