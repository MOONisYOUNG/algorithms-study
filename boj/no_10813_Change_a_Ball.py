import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [num for num in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    arr[i], arr[j] = arr[j], arr[i]
    
for data in arr[1:]:
    print(data, end=' ')