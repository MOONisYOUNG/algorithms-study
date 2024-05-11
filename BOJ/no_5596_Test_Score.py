import sys
input = sys.stdin.readline

minkook_total = sum(map(int, input().split()))
manse_total = sum(map(int, input().split()))

# max 함수는 a, b 값이 동일할 경우에 a 값을 출력
answer = max(minkook_total, manse_total)
print(answer)