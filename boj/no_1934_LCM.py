# 1. A와 B의 최대공약수를 구한 후, gcd_val 변수에 저장한다.
# 2. answer = A  * B // gcd_val를 구한다.

import sys
from math import gcd

input = sys.stdin.readline

T = int(input())

def solution():
    gcd_val = gcd(A, B)
    answer = A * B // gcd_val
    return answer

for _ in range(T):
    A, B = map(int, input().split())
    print(solution())