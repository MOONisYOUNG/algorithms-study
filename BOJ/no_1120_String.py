import sys
input = sys.stdin.readline

a, b = input().split()

result=[]

# 범위 : 0 ~ a와 b 사이에 존재하는 길이 차
for i in range(len(b)-len(a)+1):
    cnt=0
    for j in range(len(a)):
        if a[j] != b[j+i]:
            cnt+=1
    result.append(cnt)

answer = min(result)

print(answer)