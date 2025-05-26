import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def solution(a: int, b: int) -> int:
    num_li = []
    num = 1
    num_cnt = 0
    
    while len(num_li) < 1000:
        num_li.append(num)
        num_cnt += 1
        
        if num == num_cnt:
            num += 1
            num_cnt = 0
            
    answer = sum(num_li[:b]) - sum(num_li[:a-1])
    return answer
    
print(solution(a, b))