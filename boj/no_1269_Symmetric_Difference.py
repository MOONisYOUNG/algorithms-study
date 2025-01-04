# 1. A 집합과 B 집합 정보를 각각 저장한다.
# 2. answer = len((A-B) | (B-A))를 연산해서 답을 구한다.

import sys
input = sys.stdin.readline

A_cnt, B_cnt = map(int, input().split())

A = set(input().split())
B = set(input().split())

answer = len((A-B) | (B-A))
print(answer)