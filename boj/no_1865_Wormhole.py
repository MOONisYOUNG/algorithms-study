import sys
from typing import List, Tuple
input = sys.stdin.readline

def bellman_ford(n: int, edges: List[Tuple[int, int, int]]) -> bool:
    distances = [0] * (n + 1)
    
    for i in range(n - 1):
        for start, end, weight in edges:
            if distances[start] + weight < distances[end]:
                distances[end] = distances[start] + weight
    
    for start, end, weight in edges:
        if distances[start] + weight < distances[end]:
            return True
    
    return False

def solution(tc_cnt: int) -> List[str]:
    answer_li = []
    for _ in range(tc_cnt):
        n, m, w = map(int, input().split())
        
        edges = []
        
        for _ in range(m):
            s, e, t = map(int, input().split())
            edges.append((s, e, t))
            edges.append((e, s, t))
        
        for _ in range(w):
            s, e, t = map(int, input().split())
            edges.append((s, e, -t)) 
        
        answer = 'YES' if bellman_ford(n, edges) else 'NO'
        answer_li.append(answer)
    
    return answer_li

if __name__ == "__main__":
    tc_cnt = int(input())
    print(*solution(tc_cnt), sep='\n')