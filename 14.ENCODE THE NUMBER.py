n=int(input())
res=0
f=1
while n>0:
    rem=n%10
    sq=rem**2
    if sq<10:
        res=sq*f+res
        f*=10
    else:
        res+=sq*f
        f*=100
    n//=10
print(res)