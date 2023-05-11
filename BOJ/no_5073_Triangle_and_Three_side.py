import sys

input = sys.stdin.readline

def solution():
    if a < (b + c):
        if len(list(set(tri_li))) == 1:
            return "Equilateral"
        
        elif len(list(set(tri_li))) == 2:
            return "Isosceles"
            
        else:
            return "Scalene"
    else:
        return "Invalid"
        

while True:
    tri_li = list(map(int, input().split()))
    
    tri_li.sort(reverse=True)
    
    a, b, c = tri_li
    
    if a == 0 and b == 0 and c == 0:
        break
    
    print(solution())