import sys

input = sys.stdin.readline

arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))

# 1. 각 행에서 최대값을 찾는다. 이때 col 인덱스 정보도 같이 저장한다.
# 2. 각 행의 최대값끼리 비교해서 찾는다. 이때 row 인덱스 정보도 같이 찾는다.

row_max = []
for idx_1 in range(9):
    row = arr[idx_1]
    max_col_idx = 0
    
    for idx_2 in range(1, 9):
        if row[max_col_idx] < row[idx_2]:
            max_col_idx = idx_2
    row_max.append([max_col_idx, row[max_col_idx]])
    
max_row_idx = 0
for idx in range(1, 9):
    if row_max[max_row_idx][1] < row_max[idx][1]:
        max_row_idx = idx

print(row_max[max_row_idx][1])
print(max_row_idx+1, row_max[max_row_idx][0]+1, end=' ')