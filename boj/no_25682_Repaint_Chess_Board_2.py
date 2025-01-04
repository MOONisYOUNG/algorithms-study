# 0-1. 시간 제한 1초, 메모리 제한 256 MB이므로 비교적 준수한 조건이라 볼 수 있다.
# 0-2. 누적합과 다이나믹 프로그래밍을 합친 방식으로 접근하기
# 0-3. 이중 for 반복문을 2번이나 썼으므로, 반복문 캐싱을 사용하는 PyPy3로 동작시키는 편이 좋다.
# 1. '누적합+다이나믹 프로그래밍'을 이용해서 (0, 0) 칸부터 현재 칸까지 칠해야 하는 곳을 구한다.
# 2. 이전에 기록한 값을 이용해서 KxK에 해당하는 색칠 값을 구한다. 단, 이전 min 값과 비교해서 갱신해야 한다.

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

def solution(color):
    prefix_sum = [[0] * (M+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(M):
            if (i + j) % 2 != 0:
               value = (board[i][j] == color)
            else:
                value = (board[i][j] != color)
            prefix_sum[i+1][j+1] = prefix_sum[i][j+1] + prefix_sum[i+1][j] - prefix_sum[i][j] + value

    min_cnt = sys.maxsize        
    for i in range(1, N-K+2):
        for j in range(1, M-K+2):
            cnt = prefix_sum[i-1+K][j-1+K] - prefix_sum[i-1+K][j-1] - prefix_sum[i-1][j-1+K] + prefix_sum[i-1][j-1]
            min_cnt = min(min_cnt, cnt)
    return min_cnt
    
answer = min(solution('B'), solution('W'))
print(answer)