# 문제 3 : 복소수의 곱셈
from typing import Tuple
import sys
input = sys.stdin.readline

n = int(input())
complex_num_li = input()[:-1].split()

def parse_num(complex_num: str) -> Tuple:
	temp_num = complex_num.split('+')
	return int(temp_num[0]), int(temp_num[1][:-1])

def calculate(num_1: str, num_2: str) -> str:
	a, b = parse_num(num_1)
	c, d = parse_num(num_2)
	
	real_num = (a*c - b*d)
	img_num = (a*d + b*c)
	return f"{real_num}+{img_num}i"

result = complex_num_li[0]
for i in range(1, len(complex_num_li)):
	result = calculate(result, complex_num_li[i])

result_a, result_b = parse_num(result)
answer_a, answer_b = abs(result_a) % 100007, abs(result_b) % 100007 
print(answer_a, answer_b)
	