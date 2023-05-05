import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [0] * (N+1)

for _ in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i, j+1):
        arr[idx] = k
        
for data in arr[1:]:
    print(data, end=' ')