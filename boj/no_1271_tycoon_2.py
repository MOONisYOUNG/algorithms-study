import sys
from typing import List
input = sys.stdin.readline

m, n = map(int, input().split())

def solution_1(m: int, n: int) -> List[int]:
    return [m // n, m % n]
    
solution_2 = lambda m, n : [m // n, m % n]

print(*solution_1(m, n), sep='\n')
print(*solution_2(m, n), sep='\n')