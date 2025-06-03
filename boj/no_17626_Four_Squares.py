import sys
import math
input = sys.stdin.readline

n = int(input())

def solution_1(n: int) -> int:
    dp_table = [0] * (n + 1)
    
    for num in range(int(n ** 0.5) + 1):
        dp_table[num * num] = 1
    
    for i in range(1, n+1):
        if dp_table[i] != 0:
            continue
        
        j = 1
        while j*j <= i:
            if dp_table[i] == 0:
                dp_table[i] = dp_table[j*j] + dp_table[i - j*j]
            else:
                dp_table[i] = min(dp_table[i], dp_table[j*j] + dp_table[i - j*j])
            j += 1
    
    answer = dp_table[n]
    return answer
    
    
def solution_2(n: int) -> int
    dp_table = [0] + ([float('inf')] * 50001)
    
    for i in range(1, n+1):
        for j in range(1, int(math.sqrt(i)) + 1):
            square = j * j
            if i >= square:
                dp_table[i] = min(dp_table[i], dp_table[i-square] + 1)
                
    answer = dp_table[n]
    return answer
    
    
print(solution_1(n))
print(solution_2(n))