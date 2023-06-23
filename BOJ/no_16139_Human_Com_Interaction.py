# 0-1. 시간 제한 1초(추가 시간 없음), 메모리 제한 256 MB
# 0-2. 시간 자원이 넉넉한 편은 아니므로 메모리를 최대한 활용해야 함. --> 구간합 적용하기
# 1. 구간 단위로 각 알파벳의 누적합이 얼마인지 계산한다. 2차원 리스트 활용하기
# 2. l이 0이면 r까지의 위치만 구하면 된다. 만약 아닐 경우는 r 위치 값에서 l-1위치 값을 빼야 한다.

import sys
input = sys.stdin.readline

S = input().rstrip()
q = int(input())

arr = [[0]*26]
arr[0][ord(S[0])-97] = 1
for i in range(1,len(S)):
    arr.append(arr[-1][:])
    arr[i][ord(S[i])-97] += 1

for _ in range(q):
    alpha, l, r = list(input().split())
    l, r = map(int, [l, r])
    if l == 0:
        print(arr[r][ord(alpha)-97])
    else:
        print(arr[r][ord(alpha)-97] - arr[l-1][ord(alpha)-97])