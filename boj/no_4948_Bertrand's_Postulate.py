# 1. num_li = range(1, 123456*2+1)를 사용해서 전체 숫자들을 저장한다.
# 2. num_li 속 숫자들을 하나씩 소수 알고리즘에 넣어서 소수인지 확인해 본다.
    # 2-1. 소수라면, prime_num_li에 추가한다.
# 3. n을 입력받는다. 
# 4. prime_num_li 내에 n보다 크고 2n작거나 같은 수들이 몇 개 있는지 확인 후, answer에 저장한다.
# 5. answer를 출력한다.

# Tip 1 : 에라토스테네스의 체를 활용한 방식이 이것보다 더 효율적이므로 꼭 참고하기
# Tip 2 : 데이터 범위가 주어짐 + 반복되는 연산이 많음 --> 메모이제이션 활용 고려하기

import sys
input = sys.stdin.readline

def is_prime_num(n):
    if n == 1:
        return False
    elif n == 2:
        return True
        
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num_li = list(range(1, 123456*2+1))
prime_num_li = []

for num in num_li:
    if is_prime_num(num):
        prime_num_li.append(num)

while True:
    n = int(input())
    
    if n == 0:
        break
    
    answer = 0
    for i in prime_num_li:
        if n < i <= 2*n:
            answer += 1
            
    print(answer)