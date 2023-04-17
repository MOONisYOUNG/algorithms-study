import sys

input = sys.stdin.readline

A, B, V = map(int, input().split())

def solution(A, B, V):
    days = (V-B) / (A-B)
    if days == int(days):
        return int(days)
    else: 
        return int(days)+1
        
print(solution(A, B, V))