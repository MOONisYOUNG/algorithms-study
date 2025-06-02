import sys
from typing import List
input = sys.stdin.readline

a = int(input())
b = int(input())

def solution(a: int, b: int) -> List[int]:
    plus_result = a + b
    minus_result = a - b
    product_result = a * b
    
    answer = [plus_result, minus_result, product_result]
    return answer
    
print(*solution(a, b), sep='\n')