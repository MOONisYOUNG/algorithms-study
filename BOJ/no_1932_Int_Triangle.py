import sys

input = sys.stdin.readline

n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(d[i])):
        if j == 0:
            d[i][j] = d[i][j] + d[i-1][j]
            
        elif j == len(d[i])-1:
            d[i][j] = d[i][j] + d[i-1][j-1]
            
        else:
            d[i][j] = max(d[i-1][j-1], d[i-1][j]) + d[i][j]
        
print(max(d[-1]))