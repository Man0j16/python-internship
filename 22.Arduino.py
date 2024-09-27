l=list(map(int,input().split()))
sm=0
mx=0
for i in l:
    sm+=i
    mx=max(mx,abs(sm))
print(mx)