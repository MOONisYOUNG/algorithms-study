# 0. 시간 제한 2초, 메모리 제한 512 MB이므로 재귀(백트래킹)으로 풀어도 무방함.
# 1. 재귀함수 backtracking(depth, result, ops)를 정의한다.
    # 1-0. maximum과 minimum을 전역변수로 지정한다.
    # 1-1. if depth == N일 경우를 종료 조건으로 부여한다.
        # 1-1-1. maximum = max(result, maximum)을 연산한다.
        # 1-1-2. minimum = min(result, minimum)을 연산한다.
    # 1-2. plus, minus, multiply, divide = ops로 언패킹한다.
    # 1-3. if plus일 경우, 아래처럼 연산한다.
        # 1-3-1. backtracking(depth+1, total+A_li[depth], [plus-1, minus, multiply, divide])
    # 1-4. if minus일 경우, 아래처럼 연산한다. 
        # 1-4-1. backtracking(depth+1, total-A_li[depth], [plus, minus-1, multiply, divide])
    # 1-5. if multiply일 경우, 아래처럼 연산한다.
        # 1-5-1. backtracking(depth+1, total*A_li[depth], [plus, minus, multiply-1, divide])
    # 1-6. if divide일 경우, 아래처럼 연산한다.
        # 1-6-1. backtracking(depth+1, int(total/A_li[depth]), [plus, minus, multiply, divide-1])

# 2. backtracking(1, A_li[0], op_li)을 계산한다.
# 3. maximum과 minimum을 출력한다.

import sys
input = sys.stdin.readline

N = int(input())
A_li = list(map(int, input().split()))
op_li = list(map(int, input().split()))

maximum = sys.maxsize * -1
minimum = sys.maxsize

def backtracking(depth, result, ops):
    global maximum, minimum
    
    if depth == N:
        maximum = max(result, maximum)
        minimum = min(result, minimum)
        return
    
    plus, minus, multiply, divide = ops
    
    if plus:
        backtracking(depth+1, result+A_li[depth], [plus-1, minus, multiply, divide])
    if minus:
        backtracking(depth+1, result-A_li[depth], [plus, minus-1, multiply, divide])
    if multiply:
        backtracking(depth+1, result*A_li[depth], [plus, minus, multiply-1, divide])
    if divide:
        backtracking(depth+1, int(result/A_li[depth]), [plus, minus, multiply, divide-1])
        
backtracking(1, A_li[0], op_li)
print(maximum)
print(minimum)
    