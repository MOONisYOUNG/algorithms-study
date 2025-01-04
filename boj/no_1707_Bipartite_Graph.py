import sys
from collections import deque

input = sys.stdin.readline

K = int(input())

def BFS(graph, start):
    queue = deque()
    queue.append(start)
    if visited[start] == 0:
        visited[start] = 1
    while queue:
        v = queue.popleft()
        
        color = visited[v]
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                if color == 1:
                    visited[i] = 2
                else:
                    visited[i] = 1
            elif visited[i] == 1:
                if color == 1:
                    print("NO")
                    return False
            elif visited[i] == 2:
                if color == 2:
                    print("NO")
                    return False
    return True
    
    
for _ in range(K):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        node_a, node_b = map(int, input().split())
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)
    
    visited = [0] * (V+1)
    
    flag = 0
    for k in range(1, V+1):
        if not BFS(graph, k):
            flag = 1
            break
    if flag == 0:
        print("YES")
