import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []
for _ in range(N):
    data = int(input())
    
    if data == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
            
    else:
        heapq.heappush(heap, (abs(data), data))