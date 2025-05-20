import sys
from typing import List
input = sys.stdin.readline

sum_val, diff_val = map(int, input().split())

def solution(sum_val: int, diff_val: int) -> List[int]:
    answer_li = []
 
    x = (sum_val + diff_val) // 2
    y = (sum_val - diff_val) // 2
    
    if (y >= 0) and (x+y == sum_val) and (x-y == diff_val):
        answer_li.append(x)
        answer_li.append(y)
    else:
        answer_li.append(-1)
    
    return answer_li
    
print(*solution(sum_val, diff_val), sep=' ')