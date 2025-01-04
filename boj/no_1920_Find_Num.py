import sys

input = sys.stdin.readline

N = int(input())
data_set = set(map(int, input().split()))

M = int(input())
check_tuple = tuple(map(int, input().split()))
    
for element in check_tuple:
    if element in data_set:
        print(1)
    else:
        print(0)
