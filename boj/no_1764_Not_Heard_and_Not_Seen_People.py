# 1. not_hear_set(set)에 듣도 못한 사람들의 명단을 저장한다.
# 2. not_see_set(set)에 보도 못한 사람들의 명단을 저장한다.
# 3. not_hear_set & not_see_set을 연산해서 교집합을 구한다.
# 4. 교집합 결과값을 리스트로 변환시키고, 사전 순으로 정렬한다.
# 5. 리스트 길이를 출력한 후, 각 데이터를 하나씩 출력한다.

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

not_hear_set = set()
for _ in range(N):
    not_hear_set.add(input()[:-1])
    
not_see_set = set()
for _ in range(M):
    not_see_set.add(input()[:-1])
    
answer = sorted(list(not_hear_set & not_see_set))

print(len(answer))

for data in answer:
    print(data)