import sys

input = sys.stdin.readline

N = int(input())

A_arr = list(map(int, input().split()))

d = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if A_arr[j] < A_arr[i]:
            d[i] = max(d[i], d[j]+1)
            
print(max(d))