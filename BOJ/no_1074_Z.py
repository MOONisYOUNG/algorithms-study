import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
answer = 0

# 재귀를 사용한 분할정복 기법
def z_find(x, y, size):
    global answer
    if size == 1:
        return
    
    if (x < size/2) and (y < size/2):
        z_find(x, y, size/2)
        
    elif (x < size/2) and (y >= size/2):
        answer += (size*size / 4)
        z_find(x, y-size/2, size/2)
        
    elif (x >= size/2) and (y < size/2):
        answer += (size*size / 4) * 2
        z_find(x-size/2, y, size/2)
    
    else:
        answer += (size*size / 4) * 3
        z_find(x-size/2, y-size/2, size/2)
        

z_find(r, c, 2**n)
print(int(answer)) 