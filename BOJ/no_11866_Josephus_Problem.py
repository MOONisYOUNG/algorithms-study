import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
queue = deque([i for i in range(1, N+1)])

answer_li = []
while queue:
  queue.rotate(-1*(K-1))
  answer_li.append(queue.popleft())

print("<",end='')
for i in range(len(answer_li)-1):
    print("%d, "%answer_li[i], end='')
print(answer_li[-1], end='')
print(">")