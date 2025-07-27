import sys
from typing import List, Tuple
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node: int, distance: List[int], visited: List[bool], graph: List[List[Tuple[int, int]]]):
    visited[node] = True
    
    for next_node, weight in graph[node]:
        if not visited[next_node]:
            distance[next_node] = distance[node] + weight
            dfs(next_node, distance, visited, graph)

def solution(n: int) -> int:
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        parent, child, weight = map(int, input().split())
        graph[parent].append((child, weight))
        graph[child].append((parent, weight))

    distance1 = [0] * (n + 1)
    visited1 = [False] * (n + 1)

    root_node = 1
    dfs(root_node, distance1, visited1, graph)
    
    max_distance = 0
    farthest_node_from_root = 1
    for i in range(1, n + 1):
        if distance1[i] > max_distance:
            max_distance = distance1[i]
            farthest_node_from_root = i
    
    distance2 = [0] * (n + 1)
    visited2 = [False] * (n + 1)
    
    dfs(farthest_node_from_root, distance2, visited2, graph)
    answer = max(distance2)

    return answer

if __name__ == "__main__":
    n = int(input())
    print(solution(n))