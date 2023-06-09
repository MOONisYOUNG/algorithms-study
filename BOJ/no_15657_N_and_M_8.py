# 0-1. 시간 제한 1초, 메모리 제한 512 MB
# 0-2. 시간, 메모리 자원 모두 넉넉하므로 재귀로 풀어도 무방함.
# 0-3. 재귀 기반의 백트래킹으로 문제 풀이하기
# 1. num_li를 정렬한다.
# 2. s = []를 정의한다.
# 3. 재귀함수 backtracking(idx)를 정의한다.
    # 3-1. len(s) == M인 경우를 종료 조건으로 제시한다.
        # 3-1-1. ' '.join(map(str, s))를 출력한 후, return으로 종료한다.
    # 3-2. i를 매개로 idx ~ N-1까지 for 밴복문으로 순회한다.
        # 3-2-1. s.append(num_li[i])를 연산한다.
        # 3-2-2. backtracking(i)를 재귀 호출한다.
        # 3-2-3. s.pop()를 연산한다.
# 4. backtracking(0)을 연산한다.

N, M = map(int, input().split())
num_li = sorted(map(int, input().split()))

s = []

def backtracking(idx):
    if len(s) == M :
        answer = ' '.join(map(str, s))
        print(answer)
        return
    
    for i in range(idx, N):
        s.append(num_li[i])
        backtracking(i)
        s.pop()

backtracking(0)