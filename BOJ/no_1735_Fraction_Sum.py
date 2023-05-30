# 1. 두 분수 합은 다음과 같이 구한다. A/B + C/D = (A*D + B*C) / B*D
# 2. (A*D + B*C)와 B*D의 최대공약수를 구한다.
# 3. 분자와 분모 각각에 최대공약수로 나눠 준다.

from math import gcd

A, B = map(int, input().split())
C, D = map(int, input().split())

numerator = A*D + B*C
denominator = B*D

gcd_val = gcd(numerator, denominator)
numerator //= gcd_val; denominator //= gcd_val;

print(numerator, denominator)