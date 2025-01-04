# 0-1. 시간 제한 1초, 메모리 제한 512 MB
# 0-2. 시간, 메모리 모두 넉넉하므로 재귀로 풀어도 무방함.
# 0-3. 백트래킹 기법으로 접근하기
# 1. s라는 이름으로 리스트를 정의한다.
# 2. 재귀함수 solution(start)를 정의한다.
    # 2-1. 종료 조건으로 len(s) == M을 설정한다.
        # 2-1-1. answer = ' '.join(map(str, s)) 연산 후, answer을 출력한다.
    # 2-2. i를 매개로 start ~ N까지 for 반복문으로 순회한다.
        # 2-2-1. i가 s 안에 없는지 확인한다.
            # 2-2-1-1. i를 s에 추가한다.
            # 2-2-1-2. 재귀함수 solution(i+1)을 연산한다. (앞 숫자 고려할 필요 없기 때문)
            # 2-2-1-3. s.pop()을 연산한다.

N, M = map(int, input().split())
s = []

def solution(start):
    if len(s) == M:
        answer = ' '.join(map(str, s))
        print(answer)
        return
    
    for i in range(start, N+1):
        if i not in s:
            s.append(i)
            solution(i+1)
            s.pop()
          
solution(1)