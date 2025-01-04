import sys

N, K = map(int, sys.stdin.readline().split())

money_li = []
for _ in range(N):
    money_li.append(int(sys.stdin.readline()))
money_li.sort(reverse=True)

def coin_0(money_li, K):
    cnt = 0
    for money in money_li:
        cnt += K // money
        K %= money
        
    return cnt


print(coin_0(money_li, K))