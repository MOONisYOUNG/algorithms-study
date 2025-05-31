import sys
input = sys.stdin.readline

test_case_n = int(input())

def solution(n: int) -> int:
    clothes_dict = dict()
    
    for _ in range(n):
        clothes_name, clothes_category = input().split()
        if not clothes_category in clothes_dict:
            clothes_dict[clothes_category] = [clothes_name]
        else:
            clothes_dict[clothes_category].append(clothes_name)
            
    answer = 1
    for i in clothes_dict:
        answer *= (len(clothes_dict[i]) + 1)
    
    answer -= 1
    
    return answer
    
for _ in range(test_case_n):
    n = int(input())
    print(solution(n))