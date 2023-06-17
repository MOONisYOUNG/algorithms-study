# 0. 시간 제한 1초, 메모리 제한 128 MB이므로 구간합을 풀이하기에무난한 조건이다.
# 1. 구간합 리스트 sum_li를 구한다.
# 2. answer = sys.maxsize * -1으로 정의한다.
# 3. i를 매개로 0 ~ len(sum_li)-K-1까지 for 반복문을 구한다.
    # 3-1. temp = sum_li[i+K] - sum_li[i]로 K일 연속 온도 합을 구한다.
    # 3-2. if temp > answer이라면
        # 3-2-1. answer = temp로 업데이트시킨다.
# 4. answer을 출력한다.

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temparature_li = list(map(int, input().split()))

sum_li = [0]
temp = 0
for val in temparature_li:
    temp += val
    sum_li.append(temp)
    
answer = sys.maxsize * -1
for i in range(0, len(sum_li)-K):
    temp = sum_li[i+K] - sum_li[i]
    if temp > answer:
        answer = temp
print(answer)