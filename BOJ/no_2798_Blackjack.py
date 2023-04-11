import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
card_tuple = map(int, input().split())

def find_best_val(card_tuple, M):
    comb_li = []
    for comb in combinations(card_tuple, 3):
        if not sum(comb) > M:
            comb_li.append(comb)
    
    comb_li.sort(key=lambda data:-sum(data))
    return sum(comb_li[0])

print(find_best_val(card_tuple, M))