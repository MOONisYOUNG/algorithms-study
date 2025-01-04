import sys

input = sys.stdin.readline

n = int(input())

wire_li = [list(map(int, input().split())) for _ in range(n)]
wire_li.sort(key=lambda x:x[0])

wire_b = [wire[1] for wire in wire_li]

d = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if wire_b[i] > wire_b[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1
    
print(n - max(d))