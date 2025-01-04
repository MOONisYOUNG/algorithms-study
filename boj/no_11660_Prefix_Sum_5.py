# 0-1. 시간 제한 1초, 메모리 제한 256 MB <-- 메모리 자원 최대한 활용하기
# 0-2. 누적합, 동적프로그래밍으로 풀이하기 (누적합만 사용하면 시간초과 발생함)
# 1. num_arr에 숫자 행렬 값을 입력한다.  
# 2. sum_dp에 누적합 값을 저장한다.
    # 2-1. sum_dp[i][j] = sum_dp[i][j-1] + sum_dp[i-1][j] - sum_dp[i-1][j-1] + num_arr[i-1][j-1]
# 3. answer = sum_dp[x2][y2] - sum_dp[x2][y1-1] - sum_dp[x1-1][y2] + sum_dp[x1-1][y1-1]로 구할 수 있다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num_arr = [list(map(int, input().split())) for _ in range(N)]

sum_dp = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        sum_dp[i][j] = sum_dp[i][j-1] + sum_dp[i-1][j] - sum_dp[i-1][j-1] + num_arr[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    answer = sum_dp[x2][y2] - sum_dp[x2][y1-1] - sum_dp[x1-1][y2] + sum_dp[x1-1][y1-1]
    print(answer)