import sys
input = sys.stdin.readline

t = int(input())

def solution(n):
    # 11보다 작은 자연수 n의 최대값은 10이므로, d의 최대 인덱스를 10으로 지정
    d = [0] * (10+1)
    
    # d[n]은 n 값을 만들 수 있는 경우의 수를 의미
    d[0] = 1; d[1] = 1; d[2] = 2;
    
    for i in range(3, n+1):
        # d[i]는 합산 시 끝 자리가 각각 1, 2, 3인 경우를 모두를 고려하여 도출 가능
        d[i] = d[i-1] + d[i-2] + d[i-3]
    
    answer = d[n]
    return answer

for _ in range(t):
    n = int(input())
    print(solution(n))