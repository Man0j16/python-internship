from collections import defaultdict

def prime_factors(num):
    factors = defaultdict(int)
    
    while num % 2 == 0:
        factors[2] += 1
        num //= 2
    for i in range(3, int(num**0.5) + 1, 2):
        while num % i == 0:
            factors[i] += 1
            num //= i
    if num > 2:
        factors[num] += 1
    
    return factors

def calculate_prime_index_sum(arr, num):
    if not arr:
        return -1
    
    factors = prime_factors(num)
    total_sum = 0
    valid_prime_found = False
    
    for prime, power in factors.items():
        if prime < len(arr):  
            total_sum += power * arr[prime]
            valid_prime_found = True
    
    return total_sum if valid_prime_found else 0


if _name_ == "_main_":
    n = int(input())  
    arr = list(map(int, input().split()))  
    num = int(input()) 

    result = calculate_prime_index_sum(arr, num)
    print(result)