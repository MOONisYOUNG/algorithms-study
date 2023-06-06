# 0-1. 시간 제한 1초, 메모리 제한 1024 MB
# 0-2. 반복문 횟수를 늘리는 것보다 메모리 공간을 활용한 풀이를 쓰는 게 더 좋다.
# 0-3. 만약 n이 0이면, 0을 반환하도록 한다.
# 0-4. 파이썬의 round 함수 특성을 알아야 한다. 파이썬의 round 함수는 사사오입 개념이 아니다.
# 0-5. 따라서 사사오입 개념을 반영하는 my_round 함수를 따로 정의해 줘야 한다.
# 1. score_li에 score를 집어 넣는다. 
# 2. score_li.sort()를 연산한다.
# 3. cut_index = round(n * 0.15, 0)를 연산해서 절사평균 지표를 구한다.
# 4. answer = sum(score_li[cut_index : -1*cut_index]) / (n - 2*cut_index)를 연산한다.
# 5. answer = int(round(answer, 0))으로 변환시켜 줌으로써 문제 조건을 맞춰준다.

import sys
input = sys.stdin.readline

n = int(input())

def my_round(val):
    return int(val) + 1 if (val - int(val) >= 0.5) else int(val)

def solution():
    if n == 0:
        return 0
    
    else:
        score_li = [int(input()) for _ in range(n)]
        score_li.sort()
        cut_index = my_round(n * 0.15)
        
        answer = sum(score_li[cut_index : -1*cut_index] if cut_index else score_li) \
        / (n - 2*cut_index)
        answer = my_round(answer)
        return answer
        
print(solution())