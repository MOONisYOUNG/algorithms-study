import sys

input = sys.stdin.readline

N = int(input())

num_tuple = tuple(map(int, input().split()))

def is_prime_num(num):
    if num == 1:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
            
    return True
    
    
prime_cnt = 0
for num in num_tuple:
    if is_prime_num(num):
        prime_cnt += 1
print(prime_cnt)