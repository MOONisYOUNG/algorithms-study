# 0-1. 시간 제한 2초, 메모리 제한 512 MB이므로 재귀(dfs)로 풀어도 무방함.
# 0-2. 재귀 문제이므로 시간 초과를 방지하기 위해 안정적인 PyPy3를 택한다.

# 1. 연구소 그래프 정보를 data 2차원 리스트에 저장한다.
# 2. 벽 설치 완료 케이스를 임시 저장할 temp 2차원 리스트를 정의한다.
# 3. 상하좌우 4가지 이동방향을 정의한다.

# 4. 바이러스를 전염시키기 위해 virus(x, y) 재귀 함수를 정의한다.
    # 4-1. (x,y)의 상하좌우를 탐색한다. 
        # 4-1-1. 만약 새로 탐색한 자리(nx, ny)가 미로 안에 위치하고 빈 칸이면 바이러스를 배치한다.
        # 4-1-2. 새로 탐색한 자리 (nx, ny)를 기준으로 virus(nx, ny)를 재귀 호출한다.

# 5. 안전 영역 크기를 계산하기 위해 get_score() 함수를 정의한다.
    # 5-1. 초기 점수를 0으로 정의한다.
    # 5-2. 모든 영역을 다 돌아서 안전 영역의 수를 구한다. 
    # 5-3. 안전 영역 점수를 반환한다.
    
# 6. 답을 저장하기 위해 result = 0으로 할당한다.
# 7. 전체 과정을 진행할 dfs(cnt)를 정의한다.
    # result를 전역변수로 선언한다.
    # 7-0. 벽 개수가 3개일 경우 종료 조건으로 정의한다. 
        # 7-0-1. temp 리스트에 연구실 정보를 임시로 옮겨 심는다.
        # 7-0-2. 바이러스 위치에서 virus 함수를 실행한다.
        # 7-0-3. 기존 값과 새롭게 구한 안전 영역 값을 비교하여 큰 값을 rsult에 저장한다.
        # 7-0-4. return문으로 반환한다.
    # 7-1. 안전 영역에 벽을 설치하고, 벽 개수(cnt)를 하나 더한다.
    # 7-2. dfs(cnt+1) 재귀 호출함으로써 다른 영역에 벽을 설치한다. 
    # 7-3. 설치했던 벽을 철거해서 다시 안전 영역으로 만든다. 

# 8. 벽 0개 설치부터 시작하므로 dfs(0)을 실행한 후, result를 출력한다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]
temp = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx < N) and (0 <= ny < M):
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)
                
def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                score += 1
    return score

result = 0
def dfs(cnt):
    global result
    if cnt == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = data[i][j]
        
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    virus(i, j)
        
        result = max(result, get_score())
        return
    
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                data[i][j] = 1
                cnt += 1
                dfs(cnt)
                data[i][j] = 0
                cnt -= 1

dfs(0)                
print(result)