# 0. 집합 원소 포함 개수를 세야 하는 문제이므로, answer = 0으로 설정한다.
# 1. N개의 데이터를 S(set)에 저장한다.
# 2. M개의 데이터를 하나씩 집합 S 안에 있는지 확인한다.
    # 2-1. 집합 S 안에 있으면 answer += 1을 연산한다.

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

S = set()
for _ in range(N):
    S.add(input()[:-1])

answer = 0
for _ in range(M):
    data = input()[:-1]
    if data in S:
        answer += 1
        
print(answer)