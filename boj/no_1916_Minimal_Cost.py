import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

def solution(n: int, m: int) -> int:
    graph = {i:[] for i in range(1, n+1)}
    for _ in range(m):
        a, b, val = map(int, input().split())
        graph[a].append((b, val))
    
    start_node, end_node = map(int, input().split())
    
    distances = {node: float('inf') for node in range(1, n+1)}
    distances[start_node] = 0
    
    priority_queue = [(0, start_node)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    answer = distances[end_node]
    return answer
    
print(solution(n, m))