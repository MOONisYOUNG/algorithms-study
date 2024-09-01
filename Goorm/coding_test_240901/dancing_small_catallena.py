# 문제 1 : 춤추는 작은 까탈레나
from typing import Tuple
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dance_coordinate = dict()

for i in range(n):
	row = list(map(int, input().split()))
	for j in range(n):
		if row[j]:
			dance_coordinate[row[j]] = (i, j)
	
	
def calculate_distance(pos1: Tuple, pos2: Tuple) -> int:
	return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
	
	
result = 0
for i in range(1, k):
	result += calculate_distance(dance_coordinate[i], dance_coordinate[i+1])


print(result)