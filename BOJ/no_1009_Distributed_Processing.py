import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    
    # a ** b 연산 시, 4주기 단위로 1의 자리 수가 변하기 때문에 해당 식으로 간소화 가능
    b = (b % 4) + 4
    
    remainder =  (a ** b) % 10
    
    if remainder == 0:
        answer = 10
    else:
        answer = remainder
    
    print(answer)