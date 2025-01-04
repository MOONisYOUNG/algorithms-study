from typing import List
import sys
input = sys.stdin.readline

N = int(input())
goorm_knee = [list(map(int, input().split())) for _ in range(N)]

def solution(N: int, goorm_knee=List[int]) -> int:
    scar_x_set = set()
    scar_y_set = set()
    
    for i in range(N):
        for j in range(N):
            if goorm_knee[i][j]:
                scar_x_set.add(i)
                scar_y_set.add(j)

    if len(scar_x_set) == 1:
        scar_x_size = 1
    else:
        scar_x_li = list(scar_x_set)
        scar_x_li.sort()
        scar_x_size = (scar_x_li[-1] - scar_x_li[0]) + 1
        
    if len(scar_y_set) == 1:
        scar_y_size = 1
    else:
        scar_y_li = list(scar_y_set)
        scar_y_li.sort()
        scar_y_size = (scar_y_li[-1] - scar_y_li[0]) + 1

    answer = scar_x_size * scar_y_size
    return answer

print(solution(N, goorm_knee))