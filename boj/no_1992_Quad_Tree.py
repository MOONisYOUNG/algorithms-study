# 0. 시간 제한 2초, 메모리 제한 128 MB이므로 분할 정복(재귀)로 접근 가능함.
# 1. 그래프를 순회하다가 첫 칸의 색깔과 다른 칸을 만나면, 4분할로 재귀호출한다.
# 2. 만약 다른 색을 만나지 않으면 그대로 색을 출력한다. 

import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

def solution(x, y, N):
    color = graph[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if graph[i][j] != color:
                print('(', end='')
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                print(')', end='')
                return
    if color == 1:
        print(1, end='')
    else:
        print(0, end='')

solution(0, 0, N)