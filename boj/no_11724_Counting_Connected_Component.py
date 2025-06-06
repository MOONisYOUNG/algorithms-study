import sys
from typing import List
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

def solution(n: int, m: int) -> int:
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    visited = [False] * (n+1)
    connected_components = []
    
    def dfs(u: int, current_component: List[int]):
        visited[u] = True
        current_component.append(u)
        for v in graph[u]:
            if not visited[v]:
                dfs(v, current_component)
                
    for i in range(1, n+1):
        if not visited[i]:
            current_component = []
            dfs(i, current_component)
            connected_components.append(current_component)
            
    answer = len(connected_components)
    return answer
    
print(solution(n, m))