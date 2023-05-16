import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [k for k in range(1, N+1)]
for _ in range(M):
    i, j, k = map(int, input().split())
    i, j, k = i-1, j-1, k-1
    arr = arr[:i] + arr[k:j+1] + arr[i:k] + arr[j+1:]

for data in arr:
    print(data, end=' ')