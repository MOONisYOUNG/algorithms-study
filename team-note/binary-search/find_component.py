# 자료 출처 : 이것이 코딩 테스트다 (나동빈 저, 197p)

from typing import List
import sys
input = sys.stdin.readline

# Use recursive binary search (재귀 방식으로 이진 탐색 구현)
def binary_search(store_li : List, target : int, start : int, end : int) -> int :
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if target == store_li[mid]:
        return mid
    
    elif target < store_li[mid]:
        return binary_search(store_li, target, start, mid-1)
        
    else:
        return binary_search(store_li, target, mid+1, end)
    

def solution(n : int, store_li : List, m : int, cust_li : List) -> str :
    store_li.sort()
    answer = []
    for item in cust_li:
        if binary_search(store_li, item, 0, n-1):
            answer.append("yes")
        else:
            answer.append("no")
    
    return ' '.join(answer)
    

if __name__ == "__main__":
    n = int(input())
    store_li = list(map(int, input().split()))
    
    m = int(input())
    cust_li = list(map(int, input().split()))
    
    print(solution(n, store_li, m, cust_li))