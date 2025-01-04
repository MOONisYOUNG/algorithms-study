import sys

input = sys.stdin.readline

T = int(input())

def solution(k, n):
    floor_cnt = [x for x in range(1, n+1)]
    for floor_n in range(k):
        for i in range(1, n):
            floor_cnt[i] += floor_cnt[i-1]
    
    return floor_cnt[-1]
    
    
for _ in range(T):
    k = int(input())
    n = int(input())
    print(solution(k, n))