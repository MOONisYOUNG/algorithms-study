import sys
from collections import deque

Test_cnt = int(sys.stdin.readline())

def printer_queue(N, M, elements):
  queue = deque([(idx, k) for idx, k in enumerate(elements)])
  cnt = 0
  while queue:
    max_element = max(elements)
    if queue[0][1] == max_element:
      pop_element = queue.popleft()
      elements.remove(pop_element[1])
      cnt += 1
      if pop_element[0] == M:
        return cnt 
    else:
      queue.rotate(-1)


for _ in range(Test_cnt):
  N, M = map(int, sys.stdin.readline().split())
  elements = list(map(int, sys.stdin.readline().split()))
  print(printer_queue(N, M, elements))