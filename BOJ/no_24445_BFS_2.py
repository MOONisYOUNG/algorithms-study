import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for _ in range(M):
    node_a, node_b = map(int, sys.stdin.readline().split())
    graph[node_a].append(node_b)
    graph[node_b].append(node_a)


def bfs(start):
    global cnt
    queue = deque([start])
    visited[start] = cnt
    while queue:
        v = queue.popleft()
        graph[v].sort(reverse = True)
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                cnt += 1
                visited[i] = cnt
                
bfs(R)
for i in range(1, N+1):
    print(visited[i])