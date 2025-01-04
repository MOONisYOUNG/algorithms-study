import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
pop_pos_li = list(map(int, sys.stdin.readline().split()))

def rotated_queue(N, M, pop_pos_li):
  dq = deque([i for i in range(1, N+1)])
  cnt = 0
  for i in pop_pos_li:
    while True:
      if dq[0] == i:
        dq.popleft()
        break
      else:
        if dq.index(i) < len(dq)/2:
          while dq[0] != i:
            dq.rotate(-1)
            cnt += 1
        else:
          while dq[0] != i:
            dq.rotate(1)
            cnt += 1
  return cnt

print(rotated_queue(N, M, pop_pos_li))