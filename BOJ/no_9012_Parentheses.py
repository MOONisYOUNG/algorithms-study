import sys
N = int(input())

def parentheses(string):
  stack = []
  for s in string:
    if s == '(':
      stack.append(s)
    else: # s == ')'일 경우
      if not stack or stack[-1]  == ')':
        return "NO"
      stack.pop()
  if stack:
    return "NO"
  return "YES"

   
for _ in range(N):
  string = sys.stdin.readline()
  print(parentheses(string[:-1]))