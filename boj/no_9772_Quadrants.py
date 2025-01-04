import sys

input = sys.stdin.readline

def solution(x, y):
    if x == 0 or y == 0:
        return "AXIS"
    elif x > 0 and y > 0:
        return "Q1"
    elif x < 0 and y > 0:
        return "Q2"
    elif x < 0 and y < 0:
        return "Q3"
    elif x > 0 and y < 0:
        return "Q4"

while True:
    x, y = map(float, input().split())
    print(solution(x,y))
    
    if x == 0 and y == 0:
        break