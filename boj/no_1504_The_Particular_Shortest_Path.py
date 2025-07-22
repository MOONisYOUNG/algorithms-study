import sys
import heapq
from typing import List
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start: int, graph: List[List[int]], n: int) -> int:
    distance = [INF] * (n + 1)
    q = []
    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
            
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    return distance

def solution(n: int, e: int) -> int:
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    v1, v2 = map(int, input().split())
    
    dist_from_1 = dijkstra(1, graph, n)
    dist_from_v1 = dijkstra(v1, graph, n)
    dist_from_v2 = dijkstra(v2, graph, n)
    
    path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]
    path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]
    
    result = min(path1, path2)
    
    if result >= INF:
        answer = -1
    else:
        answer = result
    
    return answer

if __name__ == "__main__":
    n, e = map(int, input().split())
    print(solution(n, e))