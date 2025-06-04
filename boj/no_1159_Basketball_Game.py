import sys
input = sys.stdin.readline

n = int(input())

def solution(n: int) -> str:
    answer = ''
    first_name_dict = dict()

    for _ in range(n):
        first_name_mark = input()[0]
        if not first_name_mark in first_name_dict:
            first_name_dict[first_name_mark] = 1
        else:
            first_name_dict[first_name_mark] += 1
            
    name_li = list(filter(lambda m : first_name_dict[m] >= 5, first_name_dict.keys()))
    name_li.sort()

    if name_li:
        answer = ''.join(name_li)
    else:
        answer = 'PREDAJA'
        
    return answer
    
print(solution(n))