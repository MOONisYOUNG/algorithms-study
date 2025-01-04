import sys

input = sys.stdin.readline

N, M = map(int, input().split())
height_li = list(map(int, input().split()))

def solution(M, height_li):
    start = 0
    end = max(height_li)
    
    result = 0
    while(start <= end):
        total = 0
        mid = (start + end) // 2
        for x in height_li:
            if x > mid:
                total += x - mid
        if total < M:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    
    return result
    
    
print(solution(M, height_li))