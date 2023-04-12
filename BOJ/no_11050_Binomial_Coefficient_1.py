import sys
from itertools import combinations

input = sys.stdin.readline

N, K = map(int, input().split())
print(len(tuple(combinations(range(N), K))))