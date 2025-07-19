import sys
input = sys.stdin.readline

n = int(input())

def solution(n: int) -> int:
    board = [list(map(int, input().split())) for _ in range(n)]

    dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
    dp[0][1][0] = 1

    for r in range(n):
        for c in range(2, n):
            if board[r][c] == 0:
                dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2]

                if r > 0:
                    dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2]

                if (r > 0) and (board[r-1][c] == 0) and (board[r][c-1] == 0):
                    dp[r][c][2] = dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]

    answer = sum(dp[n-1][n-1])
    return answer

if __name__ == "__main__":
    print(solution(n))