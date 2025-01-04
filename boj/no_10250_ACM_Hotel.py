import sys

input = sys.stdin.readline

T = int(input())

def ACM_hotel(H, W, N):
    num = (N // H) + 1
    floor = N % H
    if N % H == 0:
        num = N // H
        floor = H
    return f'{floor*100 + num}'

for _ in range(T):
    H, W, N = map(int, input().split())
    print(ACM_hotel(H, W, N))