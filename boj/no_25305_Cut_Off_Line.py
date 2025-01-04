# 0. 점수 리스트(score_li)를 역으로 정렬한다.
# 1. answer = score_li[k-1]를 연산한다.

N, k = map(int, input().split())
score_li = list(map(int, input().split()))

score_li.sort(reverse=True)
answer = score_li[k-1]

print(answer)