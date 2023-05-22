# 1. 1 ~ N까지 for 반복문을 돌려서, 나누어 떨어지는 경우마다 cnt += 1을 적용한다.
    # 1-1. 만약 cnt == K이면, i를 출력한 후에 반복문을 빠져나온다.
# 2. for 반복문 내에서 return 되지 않은 경우는 0을 return 값으로 설정해 준다.

N, K = map(int, input().split())

def solution():
    cnt = 0
    for i in range(1, N+1):
        if N % i == 0:
            cnt += 1
            
        if cnt == K:
            return i
    return 0
    
print(solution())