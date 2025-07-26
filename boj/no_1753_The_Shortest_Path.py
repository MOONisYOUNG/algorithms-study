import sys
import heapq
from typing import List, Tuple
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start: int, graph: List[List[Tuple[int]]], distance: List[int]):
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

def solution(v: int, e: int, k: int) -> List[int|str]:
    graph = [[] for _ in range(v + 1)]
    distance = [INF] * (v + 1)

    for _ in range(e):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    dijkstra(k, graph, distance)

    answer = [d if d != INF else "INF" for d in distance[1:]]
    return answer

if __name__ == '__main__':
    v, e = map(int, input().split())
    k = int(input())
    print(*solution(v, e, k), sep='\n')