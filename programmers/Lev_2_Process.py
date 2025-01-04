from collections import deque
def solution(priorities, location)
    queue = deque([(idx, val) for idx, val in enumerate(priorities)])
    order = 0
    while queue
        idx, val = queue.popleft()
        
        if len(list(filter(lambda data  data[1]  val , queue))) != 0
            queue.append((idx, val))
        else
            order += 1    
            if idx == location
                return order