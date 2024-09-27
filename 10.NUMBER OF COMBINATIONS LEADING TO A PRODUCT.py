n=int(input())
l=list(map(int,input().split()))
p=int(input())
c=0
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if l[i]*l[j]*l[k]==p:
                c+=1
print(c)