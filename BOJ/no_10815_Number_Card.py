# 1. 상근이가 가진 카드 정보를 card_set에 저장한다.
# 2. data_li에 있는 값이 card_set에 있는지 확인한다.
    # 2-1. card_set에 있으면, 1을 출력한다.
    # 2-2. card_set에 없으면, 0을 출력한다.

import sys

input = sys.stdin.readline

N = int(input())
card_set = set(map(int, input().split()))

M = int(input())
data_li = list(map(int, input().split()))

for data in data_li:
    if data in card_set:
        print(1, end=' ')
    else:
        print(0, end=' ')