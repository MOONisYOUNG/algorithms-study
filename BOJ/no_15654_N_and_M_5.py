# 0-1. 시간 제한 1초, 메모리 제한 512 MB
# 0-2. 시간, 메모리 모두 넉넉하므로 재귀로 풀어도 무방하다.
# 0-3. 재귀 기반의 백트래킹으로 접근하기
# 1. num_li 를 오름차순 정렬한다.
# 2. s = []를 정의한다.
# 3. 재귀함수 backtracking()를 정의한다.
    # 3-1. len(s) == M일 경우에는 재귀함수를 종료한다.
        # 3-1-1. s에 있는 내용물을 하나의 문자열로 결합시킨 후, 출력한다.
    # 3-2. i를 매개로 0 ~ N-1까지 for 반복문으로 순회한다.
        # 3-2-1. num_li[i]가 s에 들어있지 않은 경우만 연산하기
            # 3-2-1-1. s.append(num_li[i])를 연산한다.
            # 3-2-1-2. backtracking(i+1) 재귀함수를 호출한다.
            # 3-2-1-3. s.pop()을 연산한다.
# 4. 위에서 정의한 backtracking()를 호출한다.

N, M = map(int, input().split())
num_li = sorted(map(int, input().split()))

s = []

def backtracking():
    if len(s) == M:
        answer = ' '.join(map(str, s))
        print(answer)
        return
    
    for i in range(0, N):
        if num_li[i] not in s:
            s.append(num_li[i])
            backtracking()
            s.pop()
        
backtracking()