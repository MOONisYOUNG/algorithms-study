import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

visited_DFS = [False] * (N+1)
visited_BFS = [False] * (N+1)

for _ in range(M):
    node_a, node_b = map(int, input().split())
    graph[node_a].append(node_b)
    graph[node_b].append(node_a)
    
    
def DFS(v):
    visited_DFS[v] = True
    print(v, end=' ')
    graph[v].sort()
    for i in graph[v]:
        if not visited_DFS[i]:
            DFS(i)
            
def BFS(start):
    queue = deque([start])
    visited_BFS[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        graph[v].sort()
        for i in graph[v]:
            if not visited_BFS[i]:
                queue.append(i)
                visited_BFS[i] = True
                
                
DFS(V)
print()
BFS(V)