# 0. 시간 제한 2.022초, 메모리 제한 319 MB이므로 방법론에 얽매이지 않고 문제만 풀면 된다.
# 1. 블록 1개 당 아래로 내려 갈 수 있는 경우의 수는 2이므로, 총 경우의 수는 2 ** N이다.
# 2. 따라서 answer = 2 ** N이다.

N = int(input())
answer = 2 ** N

print(answer)