# 0-1. 시간 제한 1초, 메모리 제한 512 MB
# 0-2. 시간, 메모리 모두 넉넉한 편이므로 재귀로 풀어도 무방함.
# 0-3. 백트래킹(재귀 기반)으로 문제 풀이 접근하기
# 1. s = []를 정의한다.
# 2. 재귀함수 backtracking을 정의한다.
    # 2-1. s의 길이가 M일 때를 종료조건으로 걸어준다.
        # 2-1-1. s 속 내용물을 str로 바꾼 후 결합하여 출력한다.
        # 2-1-2. return문으로 함수를 종료한다.
    # 2-2. i를 매개로 1 ~ N까지 for 반복문을 돌린다.
        # 2-2-1. s에 i를 넣는다.
        # 2-2-2. 재귀함수 backtracking을 호출한다. 
        # 2-2-3. s에 있는 내용물을 뺀다.

N, M = map(int, input().split())
s = []

def backtracking():
    if len(s) == M:
        answer = ' '.join(map(str, s))
        print(answer)
        return 
        
    for i in range(1, N+1):
        s.append(i)
        backtracking()
        s.pop()

backtracking()