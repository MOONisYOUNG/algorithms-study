# 0-1. 소수 판단 함수를 정의한다. 소수는 1과 자기자신만 약수로 갖는 수이다.
# 0-2. 소수 판단의 범위는 2 ~ int(num ** 0.5)까지이다.
# 1. M ~ N까지 for 반복문을 돌려서 소수 판단 함수를 적용한다. 소수는 리스트에 저장한다.

M = int(input())
N = int(input())

def is_prime_num(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


prime_li = []
for num in range(M, N+1):
    if is_prime_num(num):
        prime_li.append(num)
        
if not prime_li:
    print(-1)

else:
    print(sum(prime_li))
    print(prime_li[0])