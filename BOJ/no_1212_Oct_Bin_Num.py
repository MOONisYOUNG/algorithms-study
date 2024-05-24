import sys
input = sys.stdin.readline

# 8진수 --> 10진수 --> 2진수
answer = bin(int(input()[:-1], 8))[2:]
print(answer)