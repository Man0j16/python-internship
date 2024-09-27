n=int(input())
l=list(map(int,input().split()))
mx=0
for i in range(0,n):
    if i==0:
        if l[i]>l[i+1]:
            mx=i
            break
    elif i==(len(l))-1:
        if l[i]>=l[i-1]:
            mx=i
            break
    else:
        if l[i]>=l[i+1] and l[i]>=l[i-1]:
            mx=i
            break
print(mx)