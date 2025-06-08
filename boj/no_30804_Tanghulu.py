import sys
from typing import List
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
fruits_li = list(map(int, input().split()))

def solution(n: int, fruits_li: List[int]) -> int:
    answer = 0
    
    left = 0
    counts_dict = defaultdict(int)
    
    for right in range(n):
        right_num = fruits_li[right]
        counts_dict[right_num] += 1
        
        while len(counts_dict) > 2:
            left_num = fruits_li[left]
            counts_dict[left_num] -= 1
            
            if counts_dict[left_num] == 0:
                del counts_dict[left_num]
                
            left += 1
            
        answer = max(answer, right - left + 1)
        
    return answer
    
print(solution(n, fruits_li))