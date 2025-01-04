# 1-1. n == 1일 경우, answer = 4를 출력한다.
# 1-2. n != 1일 경우, answer = 4*n (이유 : 3*n + (n-1) + 1 = 4*n)를 출력한다.
# 2. 두 경우 모두 공식 하나로 일반화시킬 수 있으므로, answer = 4*n를 출력한다.

n = int(input())
answer = 4 * n
print(answer)