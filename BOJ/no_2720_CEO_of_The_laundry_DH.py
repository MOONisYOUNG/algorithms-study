import sys

input = sys.stdin.readline

T = int(input())

def solution(C):
    coins = [25, 10, 5, 1]
    
    cnt_li = []
    for worth in coins:
        cnt_li.append(C // worth)
        C %= worth
        
    for cnt in cnt_li[:-1]:
        print(cnt, end=' ')
    print(cnt_li[-1])


for _ in range(T):
    C = int(input())
    solution(C)