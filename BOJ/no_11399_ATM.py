import sys

n = int(sys.stdin.readline())
p_list = list(map(int, sys.stdin.readline().split()))

# 인출 시간을 오름차순으로 정렬
p_list.sort()

def atm(p_list):
    prefix_sum = []
    temp = 0
    for i in p_list:
        temp += i
        prefix_sum.append(temp)
    return sum(prefix_sum)


print(atm(p_list))