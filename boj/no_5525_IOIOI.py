import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()[:-1]

def solution(n: int, m: int, s: str) -> int:
    answer = 0
    current_match_len = 0
    
    for char in s:
        if current_match_len % 2 == 0:
            if char == 'I':
                current_match_len += 1
            else:
                current_match_len = 0
        else:
            if char == 'O':
                current_match_len += 1
            else:
                current_match_len = 1
                
                
        if current_match_len >= (2 * n) + 1:
            answer += 1
            current_match_len  -= 2
            
    return answer
    
print(solution(n, m, s))