# 0-1. 시간 제한 1초, 메모리 제한 512 MB
# 0-2. 시간, 메모리 자원 모두 넉넉하므로 재귀로 풀어도 무방함.
# 0-3. 재귀 기반의 백트래킹으로 풀이하기
# 1. num_li를 오름차순 정렬한다.
# 2. s = []와 visited = [False] * N을 정의한다.
# 3. 재귀함수 backtracking()를 정의한다.
    # 3-1. if len(s) == M인 경우를 종료 조건으로 제시한다.
        # 3-1-1. print(*s)로 답을 출력한다.
        # 3-1-3. return으로 재귀함수를 종료한다.
    # 3-2. temp = 0으로 지정한다.
    # 3-3. i를 매개로 0 ~ N을 for 반복문으로 순회한다.
        # 3-3-1. not visited[i]이면서 temp != num_li[i]일 경우
            # 3-3-1-1. visited[i] = True로 방문 처리한다.
            # 3-3-1-2. s.append(num_li[i])를 연산한다.
            # 3-3-1-3. temp = num_li[i]로 지정해서 for 순회 시에 예외처리할 수 있게 한다.
            # 3-3-1-4. backtracking()를 재귀 호출한다.
            # 3-3-1-5. visited[i] = False 처리해서 방문 처리를 해제한다. 
            # 3-3-1-6. s.pop()을 연산한다.
# 4. backtracking(0)을 연산한다.

N, M = map(int, input().split())
num_li = sorted(map(int, input().split()))

visited = [False] * N
s = []

def backtracking():
    if len(s) == M:
        print(*s)
        return
    
    temp = 0
    for i in range(0, N):
        if not visited[i] and temp != num_li[i]:
            visited[i] = True
            s.append(num_li[i])
            temp = num_li[i]
            
            backtracking()
            
            visited[i] = False
            s.pop()
            
backtracking()