import sys
import math
from typing import List
input = sys.stdin.readline

n =  int(input())
t_shirt_size = list(map(int, input().split()))
t, p = map(int, input().split())
    
def solution_step_1(t_shirt_size: List[int], t: int) -> int:
    answer = 0
    for size in t_shirt_size:
        answer += math.ceil(size / t)
        
    return answer
    
def solution_step_2(n: int, p: int) -> List[int]:
    answer = [n // p, n % p]
    return answer
    
print(solution_step_1(t_shirt_size, t))
print(*solution_step_2(n, p), sep=' ')