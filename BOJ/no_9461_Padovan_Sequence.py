import sys

input = sys.stdin.readline

T = int(input())

def num_sequence(N):
    global dp
    if N in (1, 2, 3):
        dp[N] = 1
    
    elif N in (4, 5):
        dp[N] = 2
    
    else:
        dp[N] = dp[N-2] + dp[N-3]

for _ in range(T):
    N = int(input())
    dp = [0] * (N+1)
    
    for num in range(1, N+1):
        num_sequence(num)
        
    print(dp[N])