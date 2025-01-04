# 0. 시간 제한 2초, 메모리 제한 128 MB이므로 어떤 방식으로 풀어도 넉넉한 자원이긴 함.
# 1. 이중 반복문을 사용해서 각 인풋 값들의 요소를 차례대로 비교한다.

import sys
input = sys.stdin.readline

N = int(input())

input_li = [input().rstrip() for _ in range(N)]

answer = ''
for i in range(len(input_li[0])):
    temp = input_li[0][i]
    
    for k in range(1, N):
        if input_li[k-1][i] == input_li[k][i]:
            continue
        else:
            temp = '?'
            break
        
    answer += temp
    
print(answer)