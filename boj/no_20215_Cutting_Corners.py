w, h = map(int, input().split())

diagonal_cutting = (w**2 + h**2) ** 0.5
rectangle_cutting = w + h

answer = round(rectangle_cutting - diagonal_cutting, 9)
print(answer)