import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())

def solution(N: int, K: int) -> int:
	answer = 0
	set_dict = defaultdict(set)
	
	for _ in range(K):
		calling_home, called_home = map(int, input()[:-1].split())
		set_dict[called_home].add(calling_home)
		
		if len(set_dict[called_home]) == 2:
			set_dict[called_home] = set()
			answer += 1
			
	return answer

print(solution(N, K))