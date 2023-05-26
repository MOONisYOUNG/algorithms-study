# 0. 숫자를 num_li(리스트)에 집어 넣은 후, 정렬을 실시한다.
# 1. 평균은 sum(num_li) / 5로 계산한다. (결과값은 자연수이다.)
# 2. 중앙값은 num_li[5//2]로 계산한다. (결과값은 자연수이다.)

import sys

input = sys.stdin.readline

num_li = []
for _ in range(5):
    num_li.append(int(input()))
    
num_li.sort()

answer_1 = int(sum(num_li) / 5)
answer_2 = num_li[5//2]

print(answer_1)
print(answer_2)