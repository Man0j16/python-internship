n=int(input())
num=n+1
while True:
    is_prime=True
    if num>1:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            print(num)
            break
    num+=1