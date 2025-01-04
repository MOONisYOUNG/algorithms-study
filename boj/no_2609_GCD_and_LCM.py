import sys
from math import gcd

input = sys.stdin.readline

num1, num2 = map(int, input().split())

gcd_num = gcd(num1, num2) 
lcm_num =  gcd_num * (num1 // gcd_num) * (num2 // gcd_num)

print(gcd_num)
print(lcm_num)