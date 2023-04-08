import sys

input = sys.stdin.readline

def right_triangle(a, b, c):
    eliment_li = [a, b, c]
    eliment_li.sort()
    if eliment_li[-1]**2 == eliment_li[0]**2 + eliment_li[1]**2:
        return True
    return False


while True:
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break
    
    if right_triangle(a, b, c):
        print("right")
    else:
        print("wrong")