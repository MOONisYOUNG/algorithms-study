# 0-1. 시간 제한 1초, 메모리 제한 512 MB
# 0-2. 시간, 메모리 모두 넉넉하므로 재귀로 풀어도 무방함.
# 0-3. 재귀 기반의 백트래킹 방식으로 접근하기
# 1. 리스트 s를 정의한다.
# 2. 재귀함수 backtracking(start)을 정의한다.
    # 2-1. len(s) == M인 경우를 종료 조건으로 제시한다.
        # 2-1-1. ' '.join(map(str, s))를 연산하여 출력한다.
    # 2-2. i를 매개로 start ~ N을 for 반복문으로 순회한다.
        # 2-2-1. s.append(i)를 연산한다.
        # 2-2-2. 재귀함수 backtracking(i)를 호출한다.
        # 2-2-3. s.pop()를 연산한다.
# 3. backtracking(1)을 연산한다. 


N, M = map(int, input().split())

s = []

def backtracking(start):
    if len(s) == M:
        answer = ' '.join(map(str, s))
        print(answer)
        return
    
    for i in range(start, N+1):
        s.append(i)
        backtracking(i)
        s.pop()
        
backtracking(1)