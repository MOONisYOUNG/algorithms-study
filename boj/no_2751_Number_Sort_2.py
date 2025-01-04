import sys

input = sys.stdin.readline

N = int(input())

data_li = []
for _ in range(N):
    data_li.append(int(input()))
    
data_li.sort()
for data in data_li:
    print(data)