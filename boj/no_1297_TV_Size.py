import sys
import math
from typing import List
input = sys.stdin.readline

d, h, w = map(int, input().split())

def solution(d: int, h: int, w: int) -> List[int]:
    ratio = math.sqrt((d ** 2) / ((h ** 2) + (w ** 2)))
    answer = [int(h * ratio), int(w * ratio)]
    return answer
    
print(*solution(d, h, w), sep=' ')