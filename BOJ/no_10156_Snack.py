import sys
input = sys.stdin.readline

k, n, m = map(int, input().split())

total_price = k * n

if (total_price - m) > 0:
    answer = total_price - m
else:
    answer = 0

print(answer)