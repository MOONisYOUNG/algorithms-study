import sys
input = sys.stdin.readline

N = int(input())

def solution(a: int, b: int) -> str:
		if a % b == 0:
			return "YES"
		else:
			return "NO"
	
for _ in range(N):
	a, b = map(int, input().split())
	print(solution(a, b))