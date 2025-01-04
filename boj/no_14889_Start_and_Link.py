# 0. 시간 제한 2초, 메모리 제한 512 MB이므로 재귀(백트래킹)로 풀어도 무방함.
# 1. visited = [False] * N를 정의함으로써 방문처리 표기를 가능하게 만든다.
# 2. 가장 작은 능력치 차이 값을 구해야 하므로 min_diff = sys.maxsize를 정의한다.

# 3. 재귀함수 backtracking(depth, idx)를 정의한다.
    # 3-1. min_diff를 전역변수 선언한다.
    # 3-2. if depth == n//2를 종료 조건으로 제시한다.
        # 3-2-1. power1, power2 = 0, 0를 정의함으로써 팀 점수를 계산한다.
        # 3-2-2. i를 매개로 0 ~ n-1까지 for 반복문을 통해 순회한다.
            # 3-2-2-1. j를 매개로 0 ~ n-1까지 for 반복문을 통해 순회한다.
                # 3-2-2-1-1. if visited[i] and visited[j]라면
                    # 3-2-2-1-1. power1 += graph[i][j]를 연산한다.
                # 3-2-2-1-2. elif not visited[i] and not visited[j]라면
                    # 3-2-1-2-1. power2 += graph[i][j]를 연산한다.
        # 3-2-3. min_diff = min(min_diff, abs(power1-power2))를 연산한다.
        # 3-2-4. return문으로 재귀함수를 종료한다.
    # 3-3. i를 매개로 idx ~ n-1까지 for 반복문으로 순회한다.
        # 3-3-1. visited[i] = True로 지정한다.
        # 3-3-2. backtracking(depth+1, i+1)로 재귀 호출한다.
        # 3-3-3. visited[i] = False로 원상복구시킨다.

# 4. backtracking(0, 0)를 계산한다.
# 5. min_diff를 출력한다.

import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
min_diff = sys.maxsize

def backtracking(depth, idx):
    global min_diff
    if depth == N//2:
        power1, power2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                    
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]
        min_diff = min(min_diff, abs(power1-power2))
        return
    
    for i in range(idx, N):
        visited[i] = True
        backtracking(depth+1, i+1)
        visited[i] = False
            
backtracking(0, 0)
print(min_diff)
