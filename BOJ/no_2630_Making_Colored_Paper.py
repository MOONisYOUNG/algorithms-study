# 0. 시간제한 1초, 메모리 제한 128 MB이므로 재귀(분할정복)를 적용해 볼 만한 조건임.
# 1. 첫 칸 기준으로 색종이를 이루고 있는 칸을 순회한다. 
    # 1-1. 만약 색이 다른 칸이 등장하면 그 칸을 기준으로, 절반 사이즈를 적용해서 재귀 호출한다.
    # 1-2. 호출한 함수가 검사한 칸이 모두 같은 색일 경우, 색상별 색종이 수에 1을 더해준다.
    
import sys
input = sys.stdin.readline

N = int(input())
whole_paper = [list(map(int, input().split())) for _ in range(N)]
color_cnt = {0:0, 1:0}

def solution(x, y, N):
    color = whole_paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if whole_paper[i][j] != color:
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
            
    color_cnt[color] += 1

solution(0, 0, N)

print(color_cnt[0])
print(color_cnt[1])