import sys
from typing import Tuple
input = sys.stdin.readline

n = int(input())

def solution(n: int) -> Tuple[int, int]:
    max_dp = [0] * 3
    min_dp = [0] * 3
    
    row = tuple(map(int, input().split()))
    for i in range(3):
        max_dp[i] = row[i]
        min_dp[i] = row[i]
        
    for _ in range(1, n):
        row = tuple(map(int, input().split()))
        
        current_max_dp = [0] * 3
        current_min_dp = [0] * 3
        
        current_max_dp[0] = row[0] + max(max_dp[0], max_dp[1])
        current_min_dp[0] = row[0] + min(min_dp[0], min_dp[1])
        
        current_max_dp[1] = row[1] + max(max_dp[0], max_dp[1], max_dp[2])
        current_min_dp[1] = row[1] + min(min_dp[0], min_dp[1], min_dp[2])
        
        current_max_dp[2] = row[2] + max(max_dp[1], max_dp[2])
        current_min_dp[2] = row[2] + min(min_dp[1], min_dp[2])
        
        max_dp = current_max_dp
        min_dp = current_min_dp
        
    answer = (max(max_dp), min(min_dp))
    return answer
    
print(*solution(n), sep=' ')