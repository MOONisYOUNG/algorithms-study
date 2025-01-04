# 0-1. 시간 제한 2초, 메모리 제한 512 MB이므로 BFS로 풀어도 무방함.
# 1. 큐를 정의한다. 빈 큐에 A를 넣는다.
# 2. 앞에서 큐 내용물을 빼서 연산했을 때, B가 될 때까지 반복한다.
    # 2-1. 연산 내용물은 (연산 횟수, 연산 결과물) 형태로 저장한다. 
from collections import deque
    
A, B = map(int, input().split())

def BFS():
    queue = deque([(0, A)])
    
    while queue:
        cnt, result = queue.popleft()
        
        if result > B:
            continue
        if result == B:
            return cnt + 1
            
        queue.append((cnt+1, result*2))
        queue.append((cnt+1, int(str(result)+'1')))
        
    return -1
    
answer = BFS()
print(answer)