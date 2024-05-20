import sys, math
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    # 규현, 승환 사이의 거리
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    # 규현, 승환 반지름 차이
    subtraction = abs(r1 - r2)
        
    # 규현, 승환의 원 반경이 완전 일치하는 경우
    if (distance == 0) and (r1 == r2):
        answer = -1
    # 규현, 승환의 원 반경 교점이 2개인 경우
    elif (distance < r1 + r2) and (distance > subtraction):
        answer = 2
    # 규현, 승환의 원 반경 교점이 1개인 경우
    elif (distance == r1 + r2) or (distance == subtraction):
        answer = 1
    # 규현, 승환의 원 반경 교점이 0개인 경우
    else :
        answer = 0
        
    print(answer)