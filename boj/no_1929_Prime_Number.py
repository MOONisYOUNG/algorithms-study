import sys

input = sys.stdin.readline

M, N = map(int, input().split())

def is_prime_num(num):
    if num == 1:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
            
    return True
    
    
for num in range(M, N+1):
    if is_prime_num(num):
        print(num)