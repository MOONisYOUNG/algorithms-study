import sys
input = sys.stdin.readline

m = int(input())

def solution(m: int) -> int:
    ball_pos = 1
    
    for _ in range(m):
        x, y = map(int, input().split())
        
        if ball_pos in [x, y]:
            if ball_pos != x:
                ball_pos = x
            else:
                ball_pos = y
    
    return ball_pos
    
print(solution(m))