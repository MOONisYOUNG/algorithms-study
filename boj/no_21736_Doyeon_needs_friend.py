import sys
from typing import Union
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

def solution(n: int, m: int) -> Union[int, str]:
    visited = [([False] * m) for _ in range(n)]
    graph = []
    person_cnt = 0
    queue = deque()
    
    for i in range(n):
        graph.append(list(map(str, input()[:-1])))
        for j in range(m):
            if graph[i][j] == 'I':
                queue.append((i, j))
                visited[i][j] = True
        
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx < 0) or (ny < 0) or (nx >= n) or (ny >= m):
                continue
            
            if (visited[nx][ny]) or (graph[x][y] == 'X'):
                continue
            
            if graph[nx][ny] == 'P':
                person_cnt += 1
                
            visited[nx][ny] = True
            queue.append((nx, ny))
            
    if person_cnt == 0:
        answer = 'TT'
    else:
        answer = person_cnt
        
    return answer
    
print(solution(n, m))