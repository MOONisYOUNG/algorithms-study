import sys

input = sys.stdin.readline

K, N = map(int, input().split())
LAN_li = [int(input()) for _ in range(K)]

start, end = 1, max(LAN_li)

def cutting_LAN(start, end):
    while start <= end:
        mid = (start + end) // 2
        lines = 0
        for lan in LAN_li:
            lines += lan // mid
            
        if lines >= N:
            start = mid + 1
        else:
            end = mid - 1
        
    return end
    
    
print(cutting_LAN(start, end))