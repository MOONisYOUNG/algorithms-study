import sys

input = sys.stdin.readline

x_set = set()
y_set = set()

three_dots = set()
for _ in range(3):
    x, y = map(int, input().split())
    x_set.add(x)
    y_set.add(y)
    
    three_dots.add((x, y))

four_dots = set()    
for x in list(x_set):
    for y in list(y_set):
        four_dots.add((x, y))
        
for answer in list(four_dots - three_dots):
    for k in answer:
        print(k, end=' ')