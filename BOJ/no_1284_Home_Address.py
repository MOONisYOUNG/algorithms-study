import sys
input = sys.stdin.readline

def solution(N):
    # 여백 먼저 생각하기 (호수판 경계, 숫자 사이 모두 고려)
    answer = len(N) + 1
    
    for n_str in N:
        if n_str == '1':
            answer += 2
            
        elif n_str == '0':
            answer += 4
            
        else:
            answer += 3
    
    return answer


while True:
    N = input().rstrip()
    
    if N == '0':
        break
    
    print(solution(N))