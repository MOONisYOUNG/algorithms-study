import sys

T = int(sys.stdin.readline())

def parentheses(string):
  stack = []
  for s in string:
    if s == '(':
      stack.append(s)
    else:  # s == ')'일 경우
      if stack and stack[-1] == '(':
        stack.pop()
      else:
        return "NO"
  if stack:
    return "NO"
  return "YES"


for _ in range(T):
  string = sys.stdin.readline()
  print(parentheses(string[:-1]))
