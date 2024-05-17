import sys
input = sys.stdin.readline

time_li = [int(input()) for _ in range(4)]
total_time = sum(time_li)

answer_1 = total_time // 60
answer_2 = total_time % 60

print(answer_1, answer_2, sep='\n')