import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

MAX = 10 ** 5
dist = [0] * (MAX+1)

def BFS():
    queue = deque()
    queue.append(N)
    
    while queue:
        x = queue.popleft()
        if x == K:
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)
                
BFS()