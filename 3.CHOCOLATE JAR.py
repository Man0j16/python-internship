n=int(input())
 l=list(map(int,input().split()))
 c=0
 for i in l:
    if i%3==0:
        c+=i//3
    elif i%3!=0:
        c+=1+i//3
 print(c)
