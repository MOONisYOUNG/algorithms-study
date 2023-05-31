# 0. 탐색 범위가 넓으므로 while문을 사용하는 것이 좋다.
# 1. n 이상의 숫자 범위 내에서 소수를 찾는다. 
    # 1-1. 소수를 찾으면, 출력한 뒤에 break를 걸어서 반복문을 탈출한다.

import sys
input = sys.stdin.readline

n = int(input())

def is_prime_num():
    if num in (0, 1):
        return False
    elif num == 2:
        return True
    
    for k in range(2, int(num**0.5)+1):
        if num % k == 0:
            return False
    return True

for _ in range(n):
    num = int(input())
    while True:
        if is_prime_num():
            print(num)
            break
        else:
            num += 1