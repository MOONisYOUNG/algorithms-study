import heapq
import sys
from typing import List
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start: int, graph: List[List[int]], n: int) -> List[int]:
    distances = [INF] * (n + 1)
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)

        if dist > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distances

def solution(n: int, m: int, x: int) -> int:
    graph = [[] for _ in range(n + 1)]
    reversed_graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))
        reversed_graph[v].append((u, t))

    time_to_party = dijkstra(x, reversed_graph, n)
    time_from_party = dijkstra(x, graph, n)

    max_total_time = 0
    for i in range(1, n + 1):
        if i == x:
            continue
        total_time = time_to_party[i] + time_from_party[i]
        max_total_time = max(max_total_time, total_time)

    answer = max_total_time
    return answer

if __name__ == "__main__":
    n, m, x = map(int, input().split())
    print(solution(n, m, x))