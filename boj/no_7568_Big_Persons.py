import sys

input = sys.stdin.readline

N = int(input())

data_li = []
for _ in range(N):
    data_li.append(tuple(map(int, input().split())))

def solution(data_li):
    grade_li = []    
    
    for idx in range(N):
        grade = 0
        target_data = data_li[idx]
        
        for data in data_li:
            if not data == target_data:
                if target_data[0] < data[0] and target_data[1] < data[1]:
                    grade += 1
        grade_li.append(grade+1)
        
    return grade_li
    
for grade in solution(data_li):
    print(grade, end=' ')