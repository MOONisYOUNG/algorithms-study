# 0-1. 시간 제한 1초, 메모리 제한 1024MB이므로 방법론에 얽매이지 않고 문제만 풀면 된다.
# 0-2. 이왕이면 반복문 과다 사용보다, 메모리 자원을 적극적으로 활용하는 편이 더 좋다. 
# 0-3. ENTER 1회 출현했을 때를 기준으로 곰곰티콘 개수를 세야 한다.
# 1. ENTER가 주어지면, name_set = set()를 주고 continue로 넘어간다.
# 2. name_set에 유저 이름이 없으면, answer += 1을 연산하고 name_set에 유저 이름을 추가한다.
# 3. name_set에 유저 이름이 있으면, continue로 넘어간다.

import sys
input = sys.stdin.readline

N = int(input())

answer = 0
for _ in range(N):
    name = input().rstrip()
    
    if name == 'ENTER':
        name_set = set()
        continue
        
    if not name in name_set:
        answer += 1
        name_set.add(name)
    else:
        continue
    
print(answer)