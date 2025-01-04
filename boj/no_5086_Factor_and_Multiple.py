# 1. b % a == 0이면, factor를 출력한다.
# 2. a % b == 0이면, multiple를 출력한다.
# 3. 1과 2에 모두 속하지 않으면, neither를 출력한다.

import sys

input = sys.stdin.readline

def solution(a, b):
    if b % a == 0:
        return "factor"
        
    elif a % b == 0:
        return "multiple"
        
    else:
        return "neither"


while True:
    a, b = map(int, input().split())
    
    if a == 0 and b == 0:
        break
    
    print(solution(a, b))