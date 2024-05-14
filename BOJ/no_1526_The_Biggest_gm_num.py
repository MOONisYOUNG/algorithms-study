import sys
input = sys.stdin.readline

n = int(input())

# 금민수 찾기 함수
def find_gm_num(num):
    for i in str(num):
        if i not in {'4', '7'}:
            return False
    return True

for i in range(n, 0, -1):
    if find_gm_num(i):
        answer = i
        print(answer)
        break