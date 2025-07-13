import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

def solution(n: int, m: int) -> int:
    houses = []
    stores = []
    for r in range(n):
        row = tuple(map(int, input().split()))
        for c in range(n):
            if row[c] == 1:
                houses.append((r, c))
            elif row[c] == 2:
                stores.append((r, c))
                
    min_total_distance = float('inf')
    
    for num_closed in range(1, m+1):
        for operating_store_indices in combinations(range(len(stores)), m):
            operating_stores = []
            for i in operating_store_indices:
                operating_stores.append(stores[i])
            
            current_total_distance = 0
            for house_r, house_c in houses:
                min_distance_to_house = float('inf')
                for store_r, store_c in operating_stores:
                    distance = abs(house_r - store_r) + abs(house_c - store_c)
                    min_distance_to_house = min(min_distance_to_house, distance)
                current_total_distance += min_distance_to_house
        
            min_total_distance = min(min_total_distance, current_total_distance)
            
    answer = min_total_distance
    return answer
    
print(solution(n, m))