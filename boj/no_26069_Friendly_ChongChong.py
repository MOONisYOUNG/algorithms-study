# 0. 시간 제한은 1초, 메모리 제한은 1024 MB이므로 방법론에 얽매이지 않고 문제만 풀면 된다.
# 1. dance_set = {'ChongChong'}으로 기본 설정해 준다.
# 2. A 또는 B가 dance_set에 이름이 있다면, dance_set에 이름을 넣어 준다.
# 3. answer = len(list(dance_set))을 연산해서 답을 구한다.

import sys
input = sys.stdin.readline

N = int(input())
dance_set = {'ChongChong'}

for _ in range(N):
    A, B = input().split()
    
    if (A in dance_set) or (B in dance_set):
        dance_set.add(A)
        dance_set.add(B)
        
answer = len(list(dance_set))
print(answer)