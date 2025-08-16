import sys
from typing import List
input = sys.stdin.readline

def solution(r: int, c: int, t: int) -> int:
    grid = []
    air_cleaners = []
    
    for i in range(r):
        row = list(map(int, input().split()))
        grid.append(row)
        for j in range(c):
            if row[j] == -1:
                air_cleaners.append((i, j))
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def spread_dust() -> List[List[int]]:
        new_grid = [[0] * c for _ in range(r)]
        
        for row, col in air_cleaners:
            new_grid[row][col] = -1
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] > 0:
                    dust_amount = grid[i][j]
                    spread_amount = dust_amount // 5
                    spread_count = 0
                    
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if (0 <= ni < r) and (0 <= nj < c) and (grid[ni][nj] != -1):
                            new_grid[ni][nj] += spread_amount
                            spread_count += 1
                    
                    remaining = dust_amount - (spread_amount * spread_count)
                    new_grid[i][j] += remaining
        
        return new_grid
    
    def air_circulation(grid: List[List[int]]):
        top_cleaner_row = air_cleaners[0][0]
        bottom_cleaner_row = air_cleaners[1][0]
        
        for i in range(top_cleaner_row - 1, 0, -1):
            grid[i][0] = grid[i - 1][0]
        
        for j in range(c - 1):
            grid[0][j] = grid[0][j + 1]
        
        for i in range(top_cleaner_row):
            grid[i][c - 1] = grid[i + 1][c - 1]
        
        for j in range(c - 1, 1, -1):
            grid[top_cleaner_row][j] = grid[top_cleaner_row][j - 1]
        
        grid[top_cleaner_row][1] = 0
        
        for i in range(bottom_cleaner_row + 1, r - 1):
            grid[i][0] = grid[i + 1][0]
        
        for j in range(c - 1):
            grid[r - 1][j] = grid[r - 1][j + 1]
        
        for i in range(r - 1, bottom_cleaner_row, -1):
            grid[i][c - 1] = grid[i - 1][c - 1]
        
        for j in range(c - 1, 1, -1):
            grid[bottom_cleaner_row][j] = grid[bottom_cleaner_row][j - 1]
        
        grid[bottom_cleaner_row][1] = 0
    
    for _ in range(t):
        grid = spread_dust()
        air_circulation(grid)
    
    total_dust = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] > 0:
                total_dust += grid[i][j]
    
    answer = total_dust
    return answer

if __name__ == "__main__":
    r, c, t = map(int, input().split())
    print(solution(r, c, t))