import sys
N = int(sys.stdin.readline())

result = ""
long_cnt = N // 4
for _ in range(long_cnt):
  result += "long "
result += "int"

print(result)