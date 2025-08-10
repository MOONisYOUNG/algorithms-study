import sys
from collections import deque
from typing import List
input = sys.stdin.readline

def solution(n: int, k: int) -> List[int]:
    max_pos = 100000
    time = [-1] * (max_pos + 1)
    count = [0] * (max_pos + 1)
    
    queue = deque()

    if n == k:
        return [0, 1]

    time[n] = 0
    count[n] = 1
    queue.append(n)
    
    min_time = float('inf')
    
    while queue:
        x = queue.popleft()

        if time[x] > min_time:
            continue

        for pos in (x-1, x+1, x*2):
            if 0 <= pos <= max_pos:
                if time[pos] == -1:
                    time[pos] = time[x] + 1
                    count[pos] = count[x]
                    queue.append(pos)

                    if pos == k:
                        min_time = time[pos]

                elif time[pos] == (time[x] + 1):
                    count[pos] += count[x]
    
    answer = [time[k], count[k]]
    return answer

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(*solution(n, k), sep='\n')