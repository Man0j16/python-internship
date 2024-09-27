n,k,a=list(map(int,input().split()))
ans=(a+k-1)%n
if ans==0:
    print(n)
else:
    print(ans)