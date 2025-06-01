import sys
input = sys.stdin.readline

n = int(input())

def solution(n: int) -> int:
    dp_table = [0] * 1001
    
    dp_table[1] = 1
    dp_table[2] = 3
    
    for i in range(3, n+1):
        dp_table[i] = dp_table[i-1] + (2 * dp_table[i-2])
        
    answer = dp_table[n] % 10007
    return answer
    
    
print(solution(n))