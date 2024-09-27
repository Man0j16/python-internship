n=int(input())
l=list(map(int,input().split()))
f=False
ans=0
for i in range(n):
    s1=sum(l[:i])
    s2=sum(l[i+1:])
    if s1==s2:
        f=True
        ans=i
        break
if not f:
    print("NOT FOUND")
else:
    print(ans+1)