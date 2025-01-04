# 0-1. 시간 제한 0.5초, 메모리 제한 128 MB
# 0-2. 기본 방식대로 연산하면 시간 초과가 발생함. 따라서 분할 정복으로 접근해야 함.

# 1. 나머지 분배 법칙을 기반으로 식을 짠다. 
    # 1-1. 나머지 분배 법칙 : (A*B) % C = (A%C) * (B%C) % C
    
import sys

A, B, C = map(int, sys.stdin.readline().split())

def solution(A, B):
    if B == 1:
        return A % C
    else:
        tmp = solution(A, B//2)
        if B % 2 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * A) % C
            
answer = solution(A, B)
print(answer)
    