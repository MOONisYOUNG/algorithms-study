import sys
input = sys.stdin.readline
n = int(input())

def stack_sequence(n):
  stack = []
  operation_li = []
  current = 1
  
  for _ in range(n):
    num = int(input())
    while current <= num:
      stack.append(current)
      operation_li.append('+')
      current += 1
    
    if stack[-1] == num:
      stack.pop()
      operation_li.append('-')
    else:
      return "NO"
  
  return operation_li


result = stack_sequence(n)
if result == "NO":
  print(result)
else:
  for i in result:
    print(i)