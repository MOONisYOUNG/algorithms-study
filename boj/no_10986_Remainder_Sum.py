# 시간 제한 1초, 메모리 제한 256MB 
# 시간보다 메모리가 더 넉넉하므로 구간합 알고리즘 이용하기

import sys
input = sys.stdin.readline

# 문제 조건 입력하기
N, M = map(int, input().split())
num_li = list(map(int, input().split()))

# 0 ~ i까지 구간별 나머지 개수 구하기
temp_sum = 0
num_remainder = [0] * M

for i in range(N):
    temp_sum += num_li[i]
    num_remainder[temp_sum % M] += 1

# 0 ~ i까지 구간 중 합이 M으로 나누어 떨어지는 경우
result = num_remainder[0]

# 같은 나머지를 가진 2개 구간을 left와 right 기준점으로 잡으면, M으로 나누어 떨어지게 할 수 있음 (iC2 공식 적용)
for i in num_remainder:
    result += i*(i-1)//2
    
print(result)