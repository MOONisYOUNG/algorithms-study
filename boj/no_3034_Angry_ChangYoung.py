import sys

input = sys.stdin.readline

N, W, H = map(int, input().split())

def solution(match_len):
    if match_len <= max(W, H, (W**2 + H**2)**0.5):
        return "DA"
    else:
        return "NE"


for _ in range(N):
    print(solution(int(input())))