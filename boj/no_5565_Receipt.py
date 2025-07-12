import sys
input = sys.stdin.readline

total_cost = int(input())

def solution(total_cost: int) -> int:
    answer = total_cost - sum([int(input()) for _ in range(9)])
    return answer
    
print(solution(total_cost))