# 1. 100x100 사이즈의 이차 행렬을 정의한다. 이때 모든 데이터는 0으로 채운다.
# 2. 색종이 데이터를 하나씩 읽어온다.
    # 2-1. 색종이 자리에 해당하는 영역이면서, 0인 곳은 모두 1로 바꾼다.
# 3. 이차행렬의 값을 모두 더하면 검은 영역의 넓이를 구할 수 있다.

import sys

input = sys.stdin.readline

canvas = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for m in range(x, x+10):
        for n in range(y, y+10):
            if canvas[m][n] != 1:
                canvas[m][n] = 1
                
print(sum([sum(row) for row in canvas]))