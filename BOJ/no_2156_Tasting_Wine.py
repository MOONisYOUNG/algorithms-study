import sys

input = sys.stdin.readline

n = int(input())

glass_data = [int(input()) for _ in range(n)]

def solution():
    if n <= 2:
        return sum(glass_data)
        
    d = [0] * n
    
    d[0] = glass_data[0]
    d[1] = glass_data[0] + glass_data[1]
    d[2] = max(glass_data[0]+glass_data[2], glass_data[1]+glass_data[2], d[1])
    
    if n == 3:
        return d[-1]
        
    else:
        for i in range(3, n):
            d[i] = max(d[i-2]+glass_data[i], d[i-3]+glass_data[i-1]+glass_data[i], d[i-1])
        return d[-1]

print(solution())