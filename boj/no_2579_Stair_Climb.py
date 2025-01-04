import sys

input = sys.stdin.readline

N = int(input())
step_scores = [int(input()) for _ in range(N)]

def solution():
    if N <= 2:
        return sum(step_scores)
    
    else:
        d = [0] * N
        d[0] = step_scores[0]
        d[1] = step_scores[0] + step_scores[1]
        for i in range(2, N):
            d[i] = max(d[i-2]+step_scores[i], d[i-3]+step_scores[i-1]+step_scores[i])
        
        return d[-1]
    

print(solution())