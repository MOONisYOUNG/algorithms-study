# 1. 가로수 사이의 간격을 구해서 distance_li(리스트)에 저장한다. 
# 2. distance_li의 최대공약수를 구한 뒤, gcd_val에 저장한다. 
# 3. 간격 // gcd_val - 1을 통해서 간격 사이에 심을 나무의 수를 구할 수 있다. (for 반복문 사용)

import sys
from math import gcd
input = sys.stdin.readline

N = int(input())

A = int(input())
distance_li = []
for _ in range(N-1):
    B = int(input())
    distance_li.append(B-A)
    A = B

gcd_val = distance_li[0]
for dist in distance_li[1:]:
    gcd_val = gcd(gcd_val, dist)

answer = 0
for dist in distance_li:
    answer += (dist // gcd_val - 1)

print(answer)