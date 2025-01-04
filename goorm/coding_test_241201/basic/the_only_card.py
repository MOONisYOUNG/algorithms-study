import sys
from typing import List
from collections import Counter

input = sys.stdin.readline

N = int(input())
c_li = list(map(int, input().split()))

def solution(N: int, c_li: List) -> int:
	c_cnt = Counter(c_li)
	for key in c_cnt:
		if c_cnt[key] == 1:
			return key
		
print(solution(N, c_li))