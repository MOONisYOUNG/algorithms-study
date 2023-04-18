import sys

input = sys.stdin.readline

N = int(input())

data_li = []
for _ in range(N):
    data_li.append(tuple(map(int, input().split())))
    
data_li.sort(key=lambda data : (data[1],data[0]))

for data in data_li:
    print(data[0], data[1])