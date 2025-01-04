# 0-1. 시간 제한 0.5초, 메모리 제한 128 MB이므로 반복문 횟수를 최소화시켜야 한다.
# 0-2. 각 테스트 케이스마다 mCn을 계산해야 한다.
# 0-3. itertools 라이브러리의 combinations을 쓰면, 시간 초과가 발생할 가능성이 높으므로 수식을 써야 한다.
# 1. M! / ((M-N)! * N!) 수식을 사용해서 각 케이스의 answer을 구하면 된다.

import sys
from math import factorial
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    answer = int(factorial(M) / (factorial(M-N) * factorial(N)))
    print(answer)