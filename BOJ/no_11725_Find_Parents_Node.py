# 0. 시간 제한 1초, 메모리 제한 256 MB로 재귀(dfs)를 사용해도 무방하다.
# 1. 인접 리스트 형태로 graph를 구성한다.
# 2. dfs를 시행할 것이므로 방문 정보를 기록할 visited 리스트를 만든다.
# 3. 재귀 함수 dfs(s)를 정의한다. 
    # 3-1. graph[s]의 원소를 하나씩 순회한다.
        # 3-1-1. 방문한 적 없는 원소일 경우, 아래처럼 연산한다.
            # 3-1-1-1. 해당 원소의 방문 정보에 부모 노드를 저장한다.
            # 3-1-1-2. 해당 원소를 기준으로 dfs를 재실시한다.
# 4. 부모 노드인 1부터 dfs를 실시한다.
# 5. 노드 2부터 노드 N까지 순서대로 visited 정보를 출력한다.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0] * (N+1)
    
def dfs(s):
    for i in graph[s]:
        if not visited[i]:
            visited[i] = s
            dfs(i)
    
dfs(1)
print(*visited[2:], sep='\n')