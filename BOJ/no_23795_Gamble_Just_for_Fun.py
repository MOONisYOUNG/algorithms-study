import sys
input = sys.stdin.readline

money_li = []
while True:
    money = int(input())
    if money == -1:
        break
    
    money_li.append(money)
    
print(sum(money_li))