import sys

input = sys.stdin.readline

N = int(input())

def factorial(N):
    if N <= 1:
        return 1
    else:
        return N * factorial(N-1)
        
factorial_result = str(factorial(N))
zero_cnt = 0
for string in factorial_result[::-1]:
    if string == '0':
        zero_cnt += 1
    else:
        break

print(zero_cnt)