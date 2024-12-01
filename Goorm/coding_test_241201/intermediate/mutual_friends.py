import sys
from typing import List

input = sys.stdin.readline

N, M = map(int, input().split())

def solution(N: int, M: int) -> List:
	n_set = set()
	for _ in range(N):
		n_set.add(input()[:-1])
		
	m_set = set()
	for _ in range(M):
		m_set.add(input()[:-1])
		
	answer = sorted(list(n_set & m_set))
	return answer

answer = solution(N, M)
if answer:
	print(*answer, sep='\n')
else:
	print(-1)