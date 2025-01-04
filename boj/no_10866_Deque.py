import sys
from collections import deque

N = int(sys.stdin.readline())
answer_deque = deque()

for _ in range(N):
  command = sys.stdin.readline().split()
  
  if command[0] == "push_front":
    answer_deque.appendleft(int(command[1]))
  
  elif command[0] == "push_back":
    answer_deque.append(int(command[1]))
    
  elif command[0] == "pop_front":
    if answer_deque:
      print(answer_deque.popleft())
    else:
      print(-1)
  
  elif command[0] == "pop_back":
    if answer_deque:
      print(answer_deque.pop())
    else:
      print(-1)
  
  elif command[0] == "size":
    print(len(answer_deque))
  
  elif command[0] == "empty":
    if not answer_deque:
      print(1)
    else:
      print(0)
  
  elif command[0] == "front":
    if answer_deque:
      print(answer_deque[0])
    else:
      print(-1)
  
  elif command[0] == "back":
    if answer_deque:
      print(answer_deque[-1])
    else:
      print(-1)