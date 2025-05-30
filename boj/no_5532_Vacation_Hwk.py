import sys
from math import ceil
input = sys.stdin.readline

problelm_condition_li = [int(input()) for _ in range(5)]

def solution(l: int, a: int, b: int, c: int, d: int) -> int:
    korean_hwk_day = ceil(a / c)
    math_hwk_day = ceil(b / d)
    
    answer = l - max(korean_hwk_day, math_hwk_day)
    return answer
    
print(solution(*problelm_condition_li))