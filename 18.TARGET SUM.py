l=list(map(int,input().split()))
s=int(input())
ans=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==s:
            ans.append(i)
            ans.append(j)
print(ans)