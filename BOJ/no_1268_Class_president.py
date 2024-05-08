import sys
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
check_li = [[0] * n for _ in range(n)]

for i in range(5):
    for j in range(n):
        for k in range(j+1, n):
            # n x n 대칭행렬을 사용하여 대조한 정보가 같은지 체크
            if info[j][i] == info[k][i]:
                check_li[j][k] = 1
                check_li[k][j] = 1
            
cnt_li = [check_li[i].count(1) for i in range(n)]
answer = cnt_li.index(max(cnt_li)) + 1

print(answer)