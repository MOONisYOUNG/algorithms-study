import sys
from typing import List
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [list(map(str, input()[:-1])) for _ in range(n)]

def solution(n: int, graph: List[str]) -> List[int]:
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def dfs(x: int, y: int, current_color: str, visited_arr: List[bool], is_color_weakness: bool):
        
        visited_arr[x][y] = True
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if (0 <= nx < n) and (0 <= ny < n) and (not visited_arr[nx][ny]):
                next_color = graph[nx][ny]
                
                if is_color_weakness:
                    if (current_color in ['R', 'G'] and next_color in ['R', 'G']) or \
                        (current_color == 'B' and next_color == 'B'):
                            dfs(nx, ny, current_color, visited_arr, is_color_weakness)
                else:
                    if current_color == next_color:
                        dfs(nx, ny, current_color, visited_arr, is_color_weakness)
                        
    normal_regions_cnt = 0
    visited_normal = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited_normal[i][j]:
                dfs(i, j, graph[i][j], visited_normal, False)
                normal_regions_cnt += 1
                
    color_weakness_regions_cnt = 0
    visited_color_weakness = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited_color_weakness[i][j]:
                dfs(i, j, graph[i][j], visited_color_weakness, True)
                color_weakness_regions_cnt += 1
                
    answer = [normal_regions_cnt, color_weakness_regions_cnt]
    return answer
    
print(*solution(n, graph))