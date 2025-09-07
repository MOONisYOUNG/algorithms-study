import sys
from collections import deque
from typing import List
input = sys.stdin.readline

def solution(n: int, m: int) -> int:
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def bfs_air_contact(n: int, m: int) -> List[List[int]]:
        air_contact = [[0] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]
        queue = deque()
        
        for i in range(n):
            for j in range(m):
                if (i == 0) or (i == n-1) or (j == 0) or (j == m-1):
                    if grid[i][j] == 0:
                        queue.append((i, j))
                        visited[i][j] = True
        
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if (0 <= nx < n) and (0 <= ny < m):
                    if (grid[nx][ny] == 0) and (not visited[nx][ny]):
                        visited[nx][ny] = True
                        queue.append((nx, ny))

                    elif grid[nx][ny] == 1:
                        air_contact[nx][ny] += 1

        return air_contact
    
    time = 0
    
    while True:
        cheese_count = sum(row.count(1) for row in grid)
        
        if cheese_count == 0:
            break
        
        air_contact = bfs_air_contact(n, m)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and air_contact[i][j] >= 2:
                    grid[i][j] = 0
        
        time += 1
    
    answer = time
    return answer

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(solution(n, m))