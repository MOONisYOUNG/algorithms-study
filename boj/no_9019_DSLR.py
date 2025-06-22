import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def solution(a: int, b: int) -> str:
    visited = [False] * 10000
    parent = [None] * 10000
    
    queue = deque()
    
    queue.append(a)
    visited[a] = True
    
    def op_D(n: int) -> int:
        return (n * 2) % 10000
    
    def op_S(n: int) -> int:
        return (n - 1 + 10000) % 10000
        
    def op_L(n: int) -> int:
        s = str(n).zfill(4)
        return int(s[1:] + s[0])
    
    def op_R(n: int) -> int:
        s = str(n).zfill(4)
        return int(s[-1] + s[:-1])
        
    while queue:
        current_num = queue.popleft()
        
        if current_num == b:
            path = []
            
            while current_num != a:
                prev_num, op_char = parent[current_num]
                path.append(op_char)
                current_num = prev_num
                
            answer = ''.join(path[::-1])
            return answer
        
        operations = [
            (op_D(current_num), 'D'),
            (op_S(current_num), 'S'),
            (op_L(current_num), 'L'),
            (op_R(current_num), 'R'),
            ]
            
        for next_num, op_char in operations:
            if not visited[next_num]:
                visited[next_num] = True
                parent[next_num] = (current_num, op_char)
                queue.append(next_num)

for _ in range(t):
    a, b = map(int, input().split())
    print(solution(a, b))