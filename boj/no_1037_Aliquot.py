# 0. 시간 제한 2초, 메모리 제한 512 MB이므로 방법론에 얽매이지 않고 문제만 풀면 된다.
# 1. answer = min(A_li) * max(A_li)를 연산한다.

N = int(input())
A_li = list(map(int, input().split()))

answer = min(A_li) * max(A_li)
print(answer)