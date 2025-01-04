# 0-1. 시간 제한 10초, 메모리 제한 128 MB이므로 백트래킹(재귀)으로 접근해도 무방함.
# 0-2. Python3으로 제출하면 시간 초과가 발생하므로, PyPy3로 제출해야 함.
# 0-3. 몇몇 재귀 문제들은 시간 초과를 방지하고자 PyPy3로 제출해야 하는 경우가 있음.

# 1. 답 저장할 변수를 정의한다. answer = 0
# 2. 행 단위로 퀸 자리 인덱스를 저장할 수 있도록 리스트를 정의한다. row = [0] * N

# 3. n-queen 규칙을 만족하는지 확인하는 함수 is_promising(x)를 정의한다. 
    # 3-1. i를 매개로 0 ~ x-1까지 for 반복문으로 순회한다.
        # 3-1-1. False 반환 조건 1 : x번째 줄에 놓인 퀸 자리와 i번째 줄에 놓인 퀸 자리가 같을 떄
        # 3-1-2. False 반환 조건 2 : x번째 줄에 놓인 퀸자리와 i번째 줄에 놓인 퀸자리가 대각선 위치에 있을 때
    # 3-3. True 반환 조건 : False 반환 조건을 단 한 번도 만족하지 않은 경우

# 4. n-queen 조건을 만족하는 경우 수를 구하는 재귀 함수 n_queen(x)를 정의한다.
    # 4-1. answer을 전역변수 선언해서, 재귀함수 내에서 답을 구할 수 있게끔 한다.
    # 4-2. 종료 조건으로 x가 N까지 도달한 경우를 지정한다. if x == N
        # 4-2-1. 조건을 만족하면 answer += 1을 연산한다.
        # 4-2-2. return문으로 재귀함수를 종료시킨다.
    # 4-3. i를 매개로 0 ~ N-1까지 for 반복문으로 순회한다.
    # 4-4. row[x] = i를 지정해 줌으로써, x번째 줄에 queen이 어디에 위치해 있는지 기록해 준다.
    # 4-5. if is_promising(x)를 통해 x번째 줄이 n-queen 조건을 만족하는지 확인하기
        # 4-5-1. 조건을 만족했다면 n_queen(x+1)을 재귀 호출한다.
        
# 5. 0번째 줄부터 시작해야 하므로, n_queen(0)으로 연산한다.
# 6. answer 값을 출력한다.
        

N = int(input())

answer = 0
row = [0] * N

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True
    
def n_queen(x):
    global answer
    
    if x == N:
        answer += 1
        return
    
    for i in range(N):
        row[x] = i
        if is_promising(x):
            n_queen(x+1)
            
n_queen(0)
print(answer)