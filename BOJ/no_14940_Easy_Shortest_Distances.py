# 0. 시간 제한 1초, 메모리 제한 128 MB이므로 한정 자원 내에서 BFS로 풀이 가능하다.

# 1. 큐를 정의한다. queue = deque()
# 2. 갈 수 있는 땅임에도 불구하고, 도달할 수 없는 위치는 -1로 표현해야 하므로 result 2차 행렬을 따로 정의한다.
# 3. graph 정보 입력, 목표 지점(x, y) 찾기, result에 시작점과 갈 수 없는 땅 입력하기, visit 정보 입력할 리스트 정의하기
    # 3-1. i를 매개로 for 반복문을 통해 row 한 줄 단위로 입력받는다.
        # 3-1-1. j를 매개로 for 반복문을 통해 row 속 원소들을 하나씩 확인한다.
            # 3-1-1-1. row[j] == 2일 경우는 아래 작업을 해준다.
                # 3-1-1-1-1. 인덱스 정보를 큐에 넣어준다. queue.append((i,j))
                # 3-1-1-1-2. visit[i][j] = True로 방문처리를 해준다.
                # 3-1-1-1-3. result[i][j] = 0으로 값을 재할당한다.
            # 3-1-1-2. row[j] == 0일 경우는 아래 작업을 해준다.
                # 3-1-1-2-1. result[i][j] = 0으로 값을 재할당한다.
        # 3-2. graph.append(row)로 graph 정보 한 줄을 입력한다.

# 4. dx = [-1, 1, 0, 0]으로 정의하고, dy = [0, 0, -1, 1]로 정의한다.    
# 5-3-1. 큐에 내용물이 존재하는 한, 연산을 반복한다. 
    # 5-3-1-1. x, y = queue.popleft() 연산한다.
    # 5-3-1-2. i를 매개로 for 반복문을 사용하여 4방향을 탐색한다.
        # 5-3-1-2-1. nx = x + dx[i]를, ny = y + dy[i]를 연산한다.
        # 5-3-1-2-2. 0 <= nx < n 이면서 0 <= ny < m일 경우만 고려한다.
            # 5-3-1-2-2-1. graph[i][j] == 1이면서 not visit[i][j]인 경우만 고려한다.
                # 5-3-1-2-2-1-1. result[nx][ny] = result[x][y] + 1를 연산한다.
                # 5-3-1-2-2-1-2. visit[i][j] = True 연산한다.
                # 5-3-1-2-2-1-3. queue.append((nx, ny))로 탐색 정보를 갱신한다.
                
# 6. result를 줄 단위로 출력한다.

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

result = [[-1]*m for _ in range(n)]
visit = [[False]*m for _ in range(n)]
queue = deque()

graph = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 2:
            queue.append((i, j))
            visit[i][j] = True
            result[i][j] = 0
        
        if row[j] == 0:
            result[i][j] = 0
    graph.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and not visit[nx][ny]:
                result[nx][ny] = result[x][y] + 1
                visit[nx][ny] = True
                queue.append((nx, ny))

for row in result:
    print(*row)