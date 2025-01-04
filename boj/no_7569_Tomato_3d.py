import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

queue = deque()
graph = []
for x in range(H):
    temp = []
    for y in range(N):
        temp.append(list(map(int, input().split())))
        for z in range(M):
            if temp[y][z] == 1:
                queue.append((x, y, z))
    graph.append(temp)
    
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def BFS():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if (0 <= nx < H) and (0 <= ny < N) and (0 <= nz < M) and \
            graph[nx][ny][nz]==0:
                queue.append([nx, ny, nz])
                graph[nx][ny][nz] = graph[x][y][z] + 1


BFS()
result = 0
for one_matrix in graph:
    for one_row in one_matrix:
        for one_element in one_row:
            if one_element == 0:
                print(-1)
                exit(0)
        result = max(result, max(one_row))
print(result - 1)