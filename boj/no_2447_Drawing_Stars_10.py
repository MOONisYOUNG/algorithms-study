from typing import List

def solution(n: int) -> List[str]:
    if n == 1:
        return ['*']
        
    patterns = solution(n // 3)
    pattern_li = []

    for pattern in patterns: 
        pattern_li.append(pattern * 3)
        
    for pattern in patterns:
        pattern_li.append(pattern + (' '  * (n//3)) + pattern)
        
    for pattern in patterns:
        pattern_li.append(pattern * 3)
        
    return pattern_li

if __name__ == "__main__":
    n = int(input())
    print(*solution(n), sep='\n')