import sys
input = sys.stdin.readline

N = int(input())
call_time = list(map(int, input().split()))

ys_cost = 0
ms_cost = 0
for time in call_time:
    ys_portion, ys_remainder = (time // 30) + 1, time % 30
    ys_cost += ys_portion * 10
    
    ms_portion, ms_remainder = (time // 60) + 1, time % 60
    ms_cost += ms_portion * 15

if ys_cost < ms_cost:
    print('Y', ys_cost)
    
elif ys_cost == ms_cost:
    print('Y', 'M', ys_cost)

else:
    print('M', ms_cost)