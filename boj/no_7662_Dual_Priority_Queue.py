import sys
import heapq
input = sys.stdin.readline

t = int(input())

def solution(k: int) -> str:
    min_heap = []
    max_heap = []
    num_counts = {}
    
    for _ in range(k):
        op_type, num_str = input()[:-1].split()
        num = int(num_str)
        
        if op_type == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            num_counts[num] = num_counts.get(num, 0) + 1
        
        elif op_type == 'D':
            if not num_counts:
                continue
            
            if num == 1:
                while max_heap:
                    val_to_remove = -heapq.heappop(max_heap)
                    if num_counts.get(val_to_remove, 0) > 0:
                        num_counts[val_to_remove] -= 1
                        break
                    
            elif num == -1:
                while min_heap:
                    val_to_remove = heapq.heappop(min_heap)
                    if num_counts.get(val_to_remove, 0) > 0:
                        num_counts[val_to_remove] -= 1
                        break
                    
    final_max, final_min = None, None
    
    while max_heap:
        val = -heapq.heappop(max_heap)
        if num_counts.get(val, 0) > 0:
            final_max = val
            break
        
    while min_heap:
        val = heapq.heappop(min_heap)
        if num_counts.get(val, 0) > 0:
            final_min = val
            break
        
    if (final_max is None) or (final_min is None):
        answer = 'EMPTY'
    else:
        answer = ' '.join(map(str, [final_max, final_min]))
    
    return answer
    
for _ in range(t):
    k = int(input())
    answer = solution(k)
    print(answer)