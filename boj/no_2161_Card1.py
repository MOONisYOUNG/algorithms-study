import sys
from typing import List
from collections import deque
input = sys.stdin.readline

n = int(input())

# A deque is a better version of a queue but acts similarly in Python.
def solution(sol_n: int) -> List[int]:
    queue = deque(range(1, sol_n+1))
    answer_li = []
    while queue:
        answer_li.append(queue.popleft())
        if queue:
            queue.append(queue.popleft())
    return answer_li
    
print(*solution(n))