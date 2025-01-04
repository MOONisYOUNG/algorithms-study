# 1-1. enter가 들어오면, employee_set에 추가한다.
# 1-2. leave가 들어오면, employee_set에서 제외한다.
# 2. employee_li = sorted(list(employee_set), reverse=True)를 연산한다.
# 3. employee_li를 하나씩 출력한다.

import sys

input = sys.stdin.readline

n = int(input())
employee_set = set()

for _ in range(n):
    name, state = input().split()
    
    if state == "enter":
        employee_set.add(name)
    else:
        employee_set.discard(name)
        
employee_li = sorted(list(employee_set), reverse=True)
for data in employee_li:
    print(data)