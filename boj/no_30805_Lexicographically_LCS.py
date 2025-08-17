import sys
from typing import List
input = sys.stdin.readline

def solution(n: int, a: List[int], m: int, b: List[int]) -> List[int]:
    answer = []
    i, j = 0, 0
    
    while i < n and j < m:
        max_val = -1
        next_i, next_j = -1, -1
        
        for a_idx in range(i, n):
            for b_idx in range(j, m):
                if (a[a_idx] == b[b_idx]) and (a[a_idx] > max_val):
                    max_val = a[a_idx]
                    next_i, next_j = a_idx, b_idx
        
        if max_val == -1:
            break
            
        answer.append(max_val)
        i, j = next_i + 1, next_j + 1
    
    return answer

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    answer = solution(n, a, m, b)
    print(len(answer))
    if answer:
        print(*answer)
    else:
        print()