import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (10**6+1)
dp[1] = 1
dp[2] = 2

for k in range(3, N+1):
    dp[k] = (dp[k-1] + dp[k-2]) % 15746

print(dp[N])