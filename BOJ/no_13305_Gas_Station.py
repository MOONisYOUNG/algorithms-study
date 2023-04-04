import sys

N = int(sys.stdin.readline())
road_len_li = list(map(int, sys.stdin.readline().split()))
oil_price_li = list(map(int, sys.stdin.readline().split()))

def gas_station(N, road_len_li, oil_price_li):
    result = road_len_li[0] * oil_price_li[0]
    money = oil_price_li[0]
    dist = 0
    for i in range(1, N-1):
        if oil_price_li[i] < money:
            result += (money * dist)
            dist = road_len_li[i]
            money = oil_price_li[i]
        else:
            dist += road_len_li[i]
        
        if i == N-2:
            result += (money*dist)
            
    return result
    
    
print(gas_station(N, road_len_li, oil_price_li))