import sys

N = int(sys.stdin.readline())
P_list = list(map(int, sys.stdin.readline().split()))

P_list.sort()

def ATM(P_list):
    prefix_sum = []
    temp = 0
    for i in P_list:
        temp += i
        prefix_sum.append(temp)
    return sum(prefix_sum)


print(ATM(P_list))