import sys
from typing import List
from collections import deque

input = sys.stdin.readline

N = int(input())
a_li = list(map(int, input().split()))

def solution(N: int, a_li: List) -> deque:
	even_queue = deque([])
	odd_queue = deque([])
	
	for i in range(N):
		if a_li[i] % 2 == 0:
			even_queue.append(a_li[i])		
		else:
			odd_queue.appendleft(a_li[i])
		
	total_queue = even_queue + odd_queue
	return total_queue

print(*solution(N, a_li), sep=' ', end=' ')