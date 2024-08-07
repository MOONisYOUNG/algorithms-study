import sys
input = sys.stdin.readline

def solution(n: int, s: int) -> int:
    return s // (n+1)
    
while True:
    try:
        n, s = map(int, input().split())
        print(solution(n, s))
    except:
        break