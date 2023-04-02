import sys
from collections import deque

T = int(sys.stdin.readline())

def AC(p, x_li):
  x_dq = deque(x_li)
  reverse_cnt = 0
  
  for command in p:
    if command == 'R':
      reverse_cnt += 1
    elif command == 'D':
      if not x_dq:
        return "error"
      else:
        if reverse_cnt % 2 == 0:
          x_dq.popleft()
        else:
          x_dq.pop()

  if reverse_cnt % 2 == 0:
    return '[' + (','.join(x_dq)) + ']'  
  else:
    x_dq.reverse()
    return '[' + (','.join(x_dq)) + ']'


for _ in range(T):
  p = sys.stdin.readline()[:-1]
  n = int(sys.stdin.readline())
  x_li = sys.stdin.readline()[:-1]
  if x_li == "[]":
    x_li = []
  else:
    x_li = x_li[1:-1].split(',')

  print(AC(p, x_li))