import sys

N = int(sys.stdin.readline())

schedule_li = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    schedule_li.append((start, end))
    
schedule_li.sort(key = lambda data:(data[1], data[0]))

def available_seminar_schedule(N, schedule_li):
    cnt = 1
    end_time = schedule_li[0][1]
    for i in range(1, N):
        if schedule_li[i][0] >= end_time:
            cnt += 1
            end_time = schedule_li[i][1]
    return cnt
    
    
print(available_seminar_schedule(N, schedule_li))