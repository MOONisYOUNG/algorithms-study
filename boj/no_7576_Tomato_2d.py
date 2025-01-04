import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

queue = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))


def BFS():
    global graph
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
         
            
BFS()
result = 0
for one_row in graph:
    for one_element in one_row:
        if one_element == 0:
            print(-1)
            exit(0)
    result = max(result, max(one_row))

print(result - 1)