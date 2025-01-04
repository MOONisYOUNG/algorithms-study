def parentheses(string):
  stack = []
  for s in string:
    if s=='(' or s=='[':
      stack.append(s)
    elif s==')':
      if stack and stack[-1]=='(':
        stack.pop()
      else:
        return 'no'
    elif s==']':
      if stack and stack[-1]=='[':
        stack.pop()
      else:
        return 'no'
        
  if stack:
    return 'no'
  return 'yes'
 

while True:
  string = input()
  if string == '.':
    break   
  print(parentheses(string))