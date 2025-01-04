# 0. 시간 제한 1초, 메모리 제한 256 MB이므로 마음 편하게 구현하면 된다.

import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    temp_li = list(map(int, input().split()))
    student_cnt = temp_li[0]
    score_li = temp_li[1:]
    
    avg_score = sum(score_li) / student_cnt
    over_score_cnt = len([score for score in score_li if score > avg_score])
    
    answer = str(round(over_score_cnt / student_cnt * 100, 3) ) + '%'
    print(answer)