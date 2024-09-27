goals=int(input())
size=int(input())
l=list(map(int,input().split()))
mx=0
for i in range(0,len(l)):
    sub=l[i:i+size]
    k=1
    s=0
    for j in sub:
        s+=(j*k)
        k+=1
        if s>mx:
            mx=s
print(mx)