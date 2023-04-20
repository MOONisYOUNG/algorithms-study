import sys

input = sys.stdin.readline

n = int(input())
dp = list(map(int, input().split()))

for idx in range(1, n):
    dp[idx] = max(dp[idx], dp[idx-1] + dp[idx])
    
print(max(dp))