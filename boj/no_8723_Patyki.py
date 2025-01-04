num_li = list(map(int, input().split()))
num_li.sort()

a, b, c = num_li

# 정삼각형
def regular_tri():
    return (a == b and b == c and c == a)
    
# 직각 삼각형
def right_tri():
    return (a**2 + b**2 == c**2)
    
    
if not regular_tri() and not right_tri():
    print(0)
elif not regular_tri() and right_tri():
    print(1)
elif regular_tri() and not right_tri():
    print(2)