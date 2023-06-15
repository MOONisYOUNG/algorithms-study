# 0-1. 시간 제한 1초, 메모리 제한 256 MB이므로 메모리를 최대한 활용하는 풀이를 짜야 함.
# 0-2. 구간합으로 풀이 접근하기
# 0-3. i, j는 1부터 주어지므로 인덱스화시킬려면 i-1, j-1로 생각해야 한다.
# 1. sum_ li = [N_li[0], N_li[0]+N_li[1], N_li[0]+N_li[1]+N_li[2], ... ] 형태로 구간합 리스트 구하기
# 2. i -= 1; j -= 1을 연산한다.
# 3. if i == 0이라면, sum_li[j]만 가져온다.
# 4. else라면, sum_li[j] - sum_li[i-1]을 연산한다. 

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_li = list(map(int, input().split()))

sum_li = []
temp = 0
for n in N_li:
    temp += n
    sum_li.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    i -= 1; j -= 1;
    if i == 0:
        print(sum_li[j])
    else:
        print(sum_li[j] - sum_li[i-1])