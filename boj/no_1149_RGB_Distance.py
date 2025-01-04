import sys

input = sys.stdin.readline

N = int(input())

rgb_costs = list()
for _ in range(N):
    rgb_costs.append(list(map(int, input().split())))
    
d = [[1001]*3 for _ in range(N)]
d[0][0], d[0][1], d[0][2] = rgb_costs[0][0], rgb_costs[0][1], rgb_costs[0][2]

for i in range(1, N):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + rgb_costs[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + rgb_costs[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + rgb_costs[i][2]
    
print(min(d[-1]))