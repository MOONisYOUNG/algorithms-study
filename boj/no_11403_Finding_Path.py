import sys
from typing import List
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def solution(n: int) -> List[int]:
    answer = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                answer[i][j] = 1
                
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (answer[i][k] == 1) and (answer[k][j] == 1):
                    answer[i][j] = 1
    
    return answer

answer = solution(n)
for row in answer:
    print(' '.join(map(str, row)))