import sys
X = int(sys.stdin.readline())
N = int(sys.stdin.readline())

sum_result = 0
for _ in range(N):
  a, b = map(int, sys.stdin.readline().split())
  
  sum_result += (a * b)

if sum_result == X:
  print("Yes")
else:
  print("No")