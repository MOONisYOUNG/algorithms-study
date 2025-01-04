import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

visited = [False] * (N+1)

graph = [[] for _ in range(N+1)]

for _ in range(M):
    node_a, node_b = map(int, input().split())
    graph[node_a].append(node_b)
    graph[node_b].append(node_a)
    

def BFS(start):
    cnt = 0
    queue = deque([start])
    
    visited[start] = True
    while queue:
        v = queue.popleft()
        graph[v].sort()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                cnt += 1
                visited[i] = True
    return cnt
    
    
print(BFS(1))