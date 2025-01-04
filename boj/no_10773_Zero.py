import sys

N = int(input())

stack = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))