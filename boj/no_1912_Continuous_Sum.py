import sys

input = sys.stdin.readline

n = int(input())
num_li = list(map(int, input().split()))

dp = [0] * n
dp[0] = num_li[0]
for idx in range(1, n):
    dp[idx] = max(num_li[idx], dp[idx-1] + num_li[idx])
    
print(max(dp))