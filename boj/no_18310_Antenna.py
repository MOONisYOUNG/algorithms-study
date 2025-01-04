import sys
input = sys.stdin.readline
from typing import List

def solution(n: int, house_li: List) -> int:
    house_li.sort()
    answer = house_li[(n-1) // 2]
    return answer
    
    
if __name__ == "__main__":
    n = int(input())
    house_li = list(map(int, input()[:-1].split()))
    
    print(solution(n, house_li))