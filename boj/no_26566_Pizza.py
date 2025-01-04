import sys
from math import pi

input = sys.stdin.readline

n = int(input())

def solution(A1, P1, R1, P2):
    A2 = pi * (R1**2)
    if (A1 / P1) < (A2 / P2):
        return "Whole pizza"
    else:
        return "Slice of pizza"


for _ in range(n):
    A1, P1 = map(int, input().split())
    R1, P2 = map(int, input().split())
    print(solution(A1, P1, R1, P2))