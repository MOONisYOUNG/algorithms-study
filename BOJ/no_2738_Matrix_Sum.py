import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

result = []
for n in range(N):
    temp_li = []
    for m in range(M):
        temp_li.append(A[n][m] + B[n][m])
    result.append(temp_li)
    
for row in result:
    print(' '.join(map(str, row)))