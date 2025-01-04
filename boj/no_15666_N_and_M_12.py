# 0-1. 시간 제한 2초, 메모리 제한 512 MB
# 0-2. 시간, 메모리 모두 넉넉하므로 재귀로 풀어도 무방함.
# 0-3. 재귀 기반의 백트래킹 방식으로 풀이하기
# 1. num_li를 오름차순으로 정렬한다.
# 2. 빈 리스트 s를 정의한다.
# 3. 재귀함수 backtracking(start)를 정의한다.
    # 3-1. len(s) == M인 경우를 종료조건으로 제시한다.
        # 3-1-1. s에 담긴 값을 print(*s)로 출력한다. 
        # 3-1-2. return 명령문으로 backtracking 재귀함수를 종료한다.
    # 3-2. for 반복문 순회 시, 예외 처리하기 위한 용도로 temp = 0을 정의한다.
    # 3-3. i를 매개로 start ~ N-1까지 for 반복문으로 순회한다.
        # 3-3-1. temp가 num_li[i]와 같지 않은 경우만 하단 명령을 수행한다.
            # 3-3-1-1. s.append(num_li[i])를 연산한다.
            # 3-3-1-2. temp = num_li[i] 처리함으로써 예외 처리 조건에 변화를 준다.
            # 3-3-1-3. backtracking(i)를 재귀 호출한다.
            # 3-3-1-4. s.pop()을 연산한다.
# 4. backtracking(0)을 연산한다.


N, M = map(int, input().split())
num_li = sorted(map(int, input().split()))

s = []

def backtracking(start):
    if len(s) == M:
        print(*s)
        return
    
    temp = 0
    for i in range(start, N):
        if temp != num_li[i]:
            s.append(num_li[i])
            temp = num_li[i]
            
            backtracking(i)
            s.pop()
            
backtracking(0)