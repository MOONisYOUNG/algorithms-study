import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dx = [+2, +1, -1, -2, -2, -1, +1, +2]
dy = [+1, +2, +2, +1, -1, -2, -2, -1]

def BFS():
    queue = deque()
    queue.append(start_pos)
    
    while queue:
        curX, curY = queue.popleft()
        if curX == goal_pos[0] and curY == goal_pos[1]:
            print(visited[curX][curY] - 1)
            return True
        
        for i in range(8):
            nx = curX + dx[i]
            ny = curY + dy[i]
            if nx < 0 or nx >= L or ny < 0 or ny >= L:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[curX][curY] + 1
                queue.append((nx, ny))
    return False
    

for _ in range(T):
    L = int(input())
    start_pos = tuple(map(int, input().split()))
    goal_pos = tuple(map(int, input().split()))
    
    visited = [[0]*L for _ in range(L)]
    visited[start_pos[0]][start_pos[1]] = 1
    
    BFS()