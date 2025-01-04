# 0-1. 시간 제한 1초, 메모리 제한 256 MB이므로 재귀(백트래킹)으로 풀이해도 무방함.
# 0-2. 추가 제한에 'PyPy3 : 1172ms'라고 적힌 것을 통해, Python3로 제출하면 시간 초과 발생할 것을 예측할 수 있음.
# 0-3. 따라서 Python3 대신에 PyPy3로 제출해야 함.

# 1. 그래프 정보를 graph 리스트에 입력하고, 빈 칸 정보를 blank 리스트에 입력한다.
    # 1-1. 빈 칸 정보는 [빈 칸 행 인덱스, 빈 칸 열 인덱스] 형태로 저장한다. 

# 2. x번째 row에 숫자 n이 있는지 확인하는 함수 checkRow(x, n)를 정의한다. 
    # 2-1. i를 매개로 0 ~ 8까지 for 반복문을 통해 순회한다.
        # 2-1-1. if graph[x][i] == n인 경우가 있다면, False를 반환한다.
    # 2-2. False 걸린 적이 단 한 번도 없다면 True를 반환한다.
    
# 3. y번째 column에 숫자 n이 있는지 확인하는 함수 checkCol(y, n)를 정의한다. 
    # 3-1. i를 매개로 0 ~ 8까지 for 반복문을 통해 순회한다.
        # 3-1-1. if graph[i][y] == n인 경우가 있다면, False를 반환한다.
    # 3-2. False 걸린 적이 단 한 번도 없다면 True를 반환한다.
    
# 4. [x, y]가 속한 3x3 크기 사각형에 n이 있는지 확인하는 함수 checkRect(x, y, n)를 정의한다.
    # 4-1. [x, y]가 속한 사각형의 시작 row 인덱스를 연산한다. nx = x // 3 * 3
    # 4-2. [x, y]가 속한 사각형의 시작 col 인덱스를 연산한다. ny = y // 3 * 3
    # 4-3 i를 매개로 0 ~ 2까지 for 반복문을 통해 순회한다.
        # 4-3-1. j를 매개로 0 ~ 2까지 for 반복문을 통해 순회한다.
            # 4-3-1-1. if graph[nx + i][ny + j] == n인 경우가 있다면, False를 반환한다.
    # 4-4. False 걸린 적이 단 한 번도 없다면 True를 반환한다.
    
# 5. n번째 blank를 채워넣는 함수 solution(n)를 정의한다.
    # 5-1. if n == len(blank)을 종료 조건으로 제시한다. blank는 0번째 ~ n-1번째까지 있기 때문이다.
        # 5-1-1. graph를 한 줄 단위로 출력한다. 
        # 5-1-2. exit(0)을 통해 재귀함수를 완전 종료한다. (return으로 끝내면 다른 경우의 수까지 계산하기 때문에 ...)
    # 5-2. x 좌표, y 좌표를 구한다. x, y = blank[n]
    # 5-3. i를 매개로 1 ~ 9까지 for 반복문으로 순회한다.
        # 5-3-1. checkRow(x, i)와 checkCol(y, i)와 checkRect(x, y, i) 상태를 확인한다.
            # 5-3-1-1. 모두 True라면 아래 연산을 수행한다.
            # 5-3-1-2. graph[x][y] = i를 통해 graph에 값을 채워 넣는다.
            # 5-3-1-3. solution(n+1)를 재귀 호출한다. 
            # 5-3-1-4. graph[x][y] = 0으로 초기화한다. 

# 6. solution(0)을 연산한다.
            
import sys
input = sys.stdin.readline

graph = []
blank = []

for i in range(9):
    graph.append(list(map(int, input().split())))
    for j in range(9):
        if graph[i][j] == 0:
            blank.append([i, j])

def checkRow(x, n):
    for i in range(9):
        if n == graph[x][i]:
            return False
    return True
    
def checkCol(y, n):
    for i in range(9):
        if n == graph[i][y]:
            return False
    return True
    
def checkRect(x, y, n):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if n == graph[nx+i][ny+j]:
                return False
    return True 
    
def solution(n):
    if n == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)
    
    x, y = blank[n]
    for i in range(1, 10):
        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            solution(n+1)
            graph[x][y] = 0

solution(0)