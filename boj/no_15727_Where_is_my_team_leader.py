import sys
input = sys.stdin.readline

l = int(input())
if l % 5 == 0:
    answer = l // 5
else:
    answer = (l // 5) + 1
    
print(answer)