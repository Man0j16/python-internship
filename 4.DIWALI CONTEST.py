task=int(input())
time=int(input())
work=0
rem=0
tleft=240-time
for i in range(1,task+1):
    rem+=i*5
    a=tleft-rem
    if a>=0:
        work=i
print(work)