import sys
input = sys.stdin.readline

s = input()[:-1]

# 0에서 1로, 1에서 0으로 변하는 횟수
change_cnt = 0
for i in range(len(s)):
    if s[i-1] != s[i]:
        change_cnt += 1
    
# '변화 구간' 하나 당 2씩 변화 횟수가 증가
# 따라서 '변화 구간' 개수를 구하려면 변화 횟수를 2로 나눠야 함.
answer = change_cnt // 2
print(answer)