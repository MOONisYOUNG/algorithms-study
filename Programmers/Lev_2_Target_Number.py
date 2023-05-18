# BFS 풀이 (큐 사용)
from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    
    # 2가지 경우의 수를 고려해야 함 (+number인 경우, -number인 경우)
    queue.append([numbers[0], 0])
    queue.append([-1*numbers[0], 0])
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            # 2가지 경우의 수로 분기함 
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    
    return answer