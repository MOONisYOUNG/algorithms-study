from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())

def solution(N: int) -> int:
	vote_result = defaultdict(int)
	
	for _ in range(N):
		grade, vote_num	= input().split()

		if grade == 'A':
			vote_result[int(vote_num)] += 3
		elif grade == 'B':
			vote_result[int(vote_num)] += 2
		else:
			vote_result[int(vote_num)] += 1
		
	vote_result_li = sorted(vote_result.items(), key=lambda x:-x[1])
	answer = vote_result_li[0][0]
	return answer
	
print(solution(N))