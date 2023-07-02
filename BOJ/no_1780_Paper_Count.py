# 0-1. 시간제한 2초, 메모리 제한 256 MB이므로 재귀 기반의 분할정복으로 도전 가능함.
# 0-2. 반복문이 중첩되어 있는 재귀함수를 사용하므로 PyPy3를 사용하면 더 좋음.
# 1. 백준 2630번, 백준 1992번 문제의 9분할 버전이라고 생각하면서 풀면 된다.

import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

paper_cnt = {-1:0, 0:0, 1:0}

def solution(x, y, N):
    num = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if paper[i][j] != num:
                solution(x, y, N//3)
                solution(x, y+N//3, N//3)
                solution(x, y+2*N//3, N//3)
                
                solution(x+N//3, y, N//3)
                solution(x+N//3, y+N//3, N//3)
                solution(x+N//3, y+2*N//3, N//3)
                
                solution(x+2*N//3, y, N//3)
                solution(x+2*N//3, y+N//3, N//3)
                solution(x+2*N//3, y+2*N//3, N//3)
                
                return
            
    paper_cnt[num] += 1

solution(0, 0, N)
print(paper_cnt[-1]); print(paper_cnt[0]); print(paper_cnt[1]);