import sys
from collections import deque
from typing import List
input = sys.stdin.readline

n, m = map(int, input().split())

def solution(n: int, m: int) -> int:
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    def bfs(graph: List[List[int]], start: int) -> int:
        friend_cnt_li = [0] * (n+1)
        visited = [start]
        queue = deque()
        queue.append(start)
        
        while queue:
            node = queue.popleft()
            for i in graph[node]:
                if i not in visited:
                    friend_cnt_li[i] = friend_cnt_li[node] + 1
                    visited.append(i)
                    queue.append(i)
        
        kevin_bacon_score = sum(friend_cnt_li)
        return kevin_bacon_score
        
    result = []
    for i in range(1, n+1):
        result.append(bfs(graph, i))
        
    answer = result.index(min(result)) + 1
    return answer
    
print(solution(n, m))