# 0. 만약 N == 1이면, 최소 직사각형을 만들 수 없으므로 answer = 0을 출력한다.
# 1. x_li = []와 y_li = []를 생성한 후, 좌표 값을 넣어준다.
# 3. answer = (max(x_li) - min(x_li)) * (max(y_li) - min(y_li))를 구한다.

import sys

input = sys.stdin.readline

N = int(input())

x_li = []
y_li = []
for _ in range(N):
    x, y = map(int, input().split())
    x_li.append(x); y_li.append(y);

answer = (max(x_li) - min(x_li)) * (max(y_li) - min(y_li))
print(answer)