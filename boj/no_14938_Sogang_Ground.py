import sys
from typing import List
input = sys.stdin.readline

def solution(n: int, m: int, r: int, items: List[int]) -> int:
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for _ in range(r):
        a, b, l = map(int, input().split())
        a -= 1 
        b -= 1
        dist[a][b] = l
        dist[b][a] = l 
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (dist[i][k] + dist[k][j]) < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    max_items = 0
    
    for start in range(n):
        total_items = 0
        for target in range(n):
            if dist[start][target] <= m:
                total_items += items[target]
        
        max_items = max(max_items, total_items)
    
    answer = max_items
    return answer

if __name__ == "__main__":
    n, m, r = map(int, input().split()) 
    items = list(map(int, input().split()))

    print(solution(n, m, r, items))