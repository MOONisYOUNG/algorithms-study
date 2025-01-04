# 문제 2 : 9와 4분의 3 정거장
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

name_dict = dict()
for _ in range(n):
	name, study_time = input()[:-1].split()
	hours, minutes = map(int, study_time.split(':'))
	study_minutes = hours*60 + minutes
	
	if not name in name_dict:
		name_dict[name] = [study_minutes]
	else:
		name_dict[name].append(study_minutes)
		
		
def calculate(name: str) -> bool:
	time_li = name_dict[name]
	total_time = sum([(time_li[i+1] - time_li[i]) for i in range(0, len(time_li), 2)])
	
	if total_time >= k*60:
		return True
	else:
		return False

	
result = 0
for name in name_dict.keys():
	if calculate(name):
		result += 1
	
print(result)