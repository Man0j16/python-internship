n=int(input())
 l=list(map(int,input().split()))
 cnt=0
 c=0
 for i in l:
    cnt+=i
    if cnt==0:
        c+=1
 print(c)