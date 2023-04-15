import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

data_li = []
for _ in range(N):
    data_li.append(int(input()))

# 산술평균
print(round(sum(data_li)/N))

# 중앙값
data_li.sort()
print(data_li[N//2])

# 최빈값
counter_data = Counter(data_li)
max_cnt = max(counter_data.values())

max_cnt_data_li = []
for key in counter_data:
    if counter_data[key] == max_cnt:
        max_cnt_data_li.append(key)

if len(max_cnt_data_li) > 1:
    print(max_cnt_data_li[1])
else:
    print(max_cnt_data_li[0])

# 범위    
print(data_li[-1] -  data_li[0])