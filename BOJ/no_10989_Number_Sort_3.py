import sys

input = sys.stdin.readline

N = int(input())
data_li = [0] * (10**4+1)
for _ in range(N):
    data_li[int(input())] += 1

for idx in range(10**4+1):
    if data_li[idx] != 0:
        for _ in range(data_li[idx]):
            print(idx)