# 0. 이전 수열 항의 밑을 k라고 하자. 
# 1. 해당 문제는 (k + (k-1)) ** 2으로 구할 수 있다.

N = int(input())

answer = 0

k = 2
for _ in range(N):
    k = k + k-1
    answer = k ** 2
    
print(answer)