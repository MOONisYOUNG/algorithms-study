import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
card_counter = Counter(map(int, input().split()))
M = int(input())

curious_tuple = tuple(map(int, input().split()))
for card in curious_tuple:
    print(card_counter[card], end=' ')