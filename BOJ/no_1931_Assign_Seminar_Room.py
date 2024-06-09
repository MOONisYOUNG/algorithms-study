import sys
input = sys.stdin.readline

n = int(input())

schedule_li = []
for _ in range(n):
    start, end = map(int, input().split())
    schedule_li.append((start, end))
    
# 회의 끝나는 시간, 회의 시작 시간 순으로 오름차순 정렬
schedule_li.sort(key = lambda data:(data[1], data[0]))
print(schedule_li)

def available_seminar_schedule(n, schedule_li):
    cnt = 1
    end_time = schedule_li[0][1]
    for i in range(1, n):
        if schedule_li[i][0] >= end_time:
            cnt += 1
            end_time = schedule_li[i][1]
    return cnt
    
    
print(available_seminar_schedule(n, schedule_li))