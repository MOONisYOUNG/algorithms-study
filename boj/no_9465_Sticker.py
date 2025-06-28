import sys
input = sys.stdin.readline

t = int(input())

def solution(n: int) -> int:
    board = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(3)]
    
    dp[0][0] = 0
    dp[1][0] = board[0][0]
    dp[2][0] = board[1][0]
    
    for j in range(1, n):
        dp[0][j] = max(dp[0][j-1], dp[1][j-1], dp[2][j-1])
        dp[1][j] = board[0][j] + max(dp[0][j-1], dp[2][j-1])
        dp[2][j] = board[1][j] + max(dp[0][j-1], dp[1][j-1])
        
    answer = max(dp[0][n-1], dp[1][n-1], dp[2][n-1])
    return answer

for _ in range(t):
    n = int(input())
    print(solution(n))