# 0-1. 컴퓨터는 무한소수를 정확히 표현하는 데에 있어서 한계가 존재함.
# 0-2. float 자료형, Decimal 자료형 모두 한계가 있음.
# 0-3. 따라서 float 자료형이 아니라 수리적으로 접근하여 하나씩 계산하는 편이 정확함.

A, B, N = map(int, input().split())

answer = 0
for i in range(N):
    A = (A%B) * 10
    answer = A // B

print(answer)