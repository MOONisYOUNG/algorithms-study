import sys
from typing import List
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def solution() -> List[int]:
    pre_oreder_li = []
    while True:
        try:
            num = int(input())
            pre_oreder_li.append(num)
        except:
            break

    post_order_li = []

    def post_order(start_idx: int, end_idx: int):
        if start_idx > end_idx:
            return

        root = pre_oreder_li[start_idx]
        
        mid_idx = end_idx + 1  
        for i in range(start_idx + 1, end_idx + 1):
            if pre_oreder_li[i] > root:
                mid_idx = i
                break

        post_order(start_idx + 1, mid_idx - 1)
        post_order(mid_idx, end_idx)
        
        post_order_li.append(root)

    
    post_order(0, len(pre_oreder_li) - 1)
    
    answer = post_order_li
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')