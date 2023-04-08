import sys

input = sys.stdin.readline

N, M = map(int, input().split())

site_dict = dict()
for _ in range(N):
    url, password = input().split()
    site_dict[url] = password


for _ in range(M):
    want_to_find = input().rstrip()
    print(site_dict[want_to_find])