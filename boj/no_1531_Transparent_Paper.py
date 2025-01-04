import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0] * 101 for _ in range(101)]

# 불투명한 종이 하나씩 직접 올리기
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            arr[i][j] += 1

answer = 0
# 불투명한 종이가 m장 넘게 올려진 부분 (==투명해진 곳) 세기 
for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j] > m:
            answer += 1
            
print(answer)