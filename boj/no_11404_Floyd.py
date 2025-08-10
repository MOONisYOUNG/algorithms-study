import sys
from typing import List
input = sys.stdin.readline

def solution(n: int, m: int) -> List[List[int]]:
    graph = [[float('inf')] * (n+1) for _ in range(n+1)]
    
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = min(graph[a][b], c)

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] == float('inf'):
                graph[a][b] = 0
    
    answer = [row[1:] for row in graph[1:]]
    return answer

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    
    answer = solution(n, m)
    for row in answer:
        print(*row, sep=' ')