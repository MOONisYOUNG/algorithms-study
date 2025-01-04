import sys
input = sys.stdin.readline

n = int(input())
f = int(input())

# N의 마지막 두 자리 수가 00이 되도록 변경
n = (n // 100) * 100

for i in range(100):
    if n % f == 0:
        answer = str(n)[-2:]
        break
    n += 1
    
print(answer)